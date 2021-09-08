library(jsonlite)
data <- fromJSON("http://localhost:5000/getallbooked")
ds <- data$booked
n.tamp <- tapply(1:nrow(ds), ds$date, length)
dates <- seq(as.Date(names(n.tamp)[1], "%Y-%m-%d"), as.Date(names(n.tamp)[length(n.tamp)], "%Y-%m-%d"), by="days")
giorni.settimana <- as.POSIXlt(dates,format="%Y-%m-%d")
dataset <- data.frame(data="*", tamponi=0)
for (row in 1:length(dates)) { 
    r <- n.tamp[toString(dates[row])]
	if (giorni.settimana$wday[row] != 0) {
		if (!is.na(r)) {
			dataset <- rbind(dataset, data.frame(data=toString(dates[row]), tamponi=r[1]))
		} else {
			dataset <- rbind(dataset, data.frame(data=toString(dates[row]), tamponi=0))}}}
dataset <- dataset[-1,]
rownames(dataset) <- NULL
print(dataset)
plot(as.Date(dataset$data, "%Y-%m-%d"), dataset$tamponi, type="l", xlab="Date", ylab="Numero di tamponi")