library(RMariaDB)
library(dotenv)

load_dot_env(file = ".env")

db.conn <- dbConnect(RMariaDB::MariaDB(), user=Sys.getenv("DBUSER"), password=Sys.getenv("DBPASS"),
                   dbname=Sys.getenv("DBNAME"), host=Sys.getenv("HOSTNAME"))

query <- "SELECT * FROM booking"
rs <- dbSendQuery(db.conn, query)
booking <- dbFetch(rs)
dbClearResult(rs)
query <- "SELECT * FROM docs"
rs <- dbSendQuery(db.conn, query)
docs <- dbFetch(rs)
dbClearResult(rs)
dbDisconnect(db.conn)

cf.docs <- docs[1]
dataset <- booking[c(4,5,7)]
dataset <- dataset[rev(order(dataset$date)),]
dataset <- subset(booking[c(4,5,7)], !is.na(time_taken))

new.dataset <- data.frame(CF="*",average_time="*")
for (cf in cf.docs$CF) {
    tmp <- head(subset(dataset, dataset$CF_M == cf), 50)
    tmp$time_taken <- as.POSIXct(tmp$time_taken,format="%T",origin="1970-01-01")
    average <- format(as.POSIXct(tapply(tmp$time_taken,tmp$CF, mean),origin="1970-01-01") - lubridate::hours(1),format="%H:%M:%S")
    if (length(average) != 0) {
        new.dataset <- rbind(new.dataset, data.frame(CF=cf,average_time=average))
    }
}

new.dataset <- new.dataset[-1,]

db.conn <- dbConnect(RMariaDB::MariaDB(), user=Sys.getenv("DBUSER"), password=Sys.getenv("DBPASS"),
                   dbname=Sys.getenv("DBNAME"), host=Sys.getenv("HOSTNAME"))

for (row in 1:nrow(new.dataset)) {
    query <- paste("UPDATE docs SET avarage_time = '",new.dataset[row, "average_time"],"' WHERE CF = '",new.dataset[row, "CF"],"'", sep="")
    rs <- dbSendQuery(db.conn, query)
}
dbClearResult(rs)
dbDisconnect(db.conn)