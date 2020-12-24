
namespace GestioneTamponi
{
    partial class Login
    {
        /// <summary>
        /// Variabile di progettazione necessaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Pulire le risorse in uso.
        /// </summary>
        /// <param name="disposing">ha valore true se le risorse gestite devono essere eliminate, false in caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Codice generato da Progettazione Windows Form

        /// <summary>
        /// Metodo necessario per il supporto della finestra di progettazione. Non modificare
        /// il contenuto del metodo con l'editor di codice.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Login));
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.panel1 = new System.Windows.Forms.Panel();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox3 = new System.Windows.Forms.PictureBox();
            this.panel2 = new System.Windows.Forms.Panel();
            this.Signin = new System.Windows.Forms.Button();
            this.usernameBox = new System.Windows.Forms.TextBox();
            this.passBox = new System.Windows.Forms.TextBox();
            this.SignupMedical = new System.Windows.Forms.LinkLabel();
            this.CheckRoles = new System.Windows.Forms.CheckedListBox();
            this.textBox3 = new System.Windows.Forms.TextBox();
            this.SignupUser = new System.Windows.Forms.LinkLabel();
            this.ForgotPassword = new System.Windows.Forms.LinkLabel();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.SystemColors.GradientActiveCaption;
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(63, 27);
            this.pictureBox1.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(143, 128);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.BackColor = System.Drawing.SystemColors.GradientActiveCaption;
            this.label1.Font = new System.Drawing.Font("Bauhaus 93", 28.2F);
            this.label1.ForeColor = System.Drawing.Color.SlateGray;
            this.label1.Location = new System.Drawing.Point(211, 102);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(134, 54);
            this.label1.TabIndex = 1;
            this.label1.Text = "Login";
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.SlateGray;
            this.panel1.Location = new System.Drawing.Point(119, 231);
            this.panel1.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(235, 10);
            this.panel1.TabIndex = 2;
            // 
            // pictureBox2
            // 
            this.pictureBox2.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox2.Image")));
            this.pictureBox2.Location = new System.Drawing.Point(63, 192);
            this.pictureBox2.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(53, 49);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox2.TabIndex = 3;
            this.pictureBox2.TabStop = false;
            // 
            // pictureBox3
            // 
            this.pictureBox3.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox3.Image")));
            this.pictureBox3.Location = new System.Drawing.Point(63, 257);
            this.pictureBox3.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.pictureBox3.Name = "pictureBox3";
            this.pictureBox3.Size = new System.Drawing.Size(53, 49);
            this.pictureBox3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox3.TabIndex = 5;
            this.pictureBox3.TabStop = false;
            // 
            // panel2
            // 
            this.panel2.BackColor = System.Drawing.Color.SlateGray;
            this.panel2.Location = new System.Drawing.Point(119, 297);
            this.panel2.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(235, 10);
            this.panel2.TabIndex = 4;
            // 
            // Signin
            // 
            this.Signin.BackColor = System.Drawing.Color.SlateGray;
            this.Signin.Font = new System.Drawing.Font("Bauhaus 93", 15F);
            this.Signin.ForeColor = System.Drawing.SystemColors.ButtonFace;
            this.Signin.Location = new System.Drawing.Point(231, 327);
            this.Signin.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Signin.Name = "Signin";
            this.Signin.Size = new System.Drawing.Size(123, 49);
            this.Signin.TabIndex = 6;
            this.Signin.Text = "Sign in";
            this.Signin.UseVisualStyleBackColor = false;
            this.Signin.Click += new System.EventHandler(this.Signin_Click);
            // 
            // usernameBox
            // 
            this.usernameBox.BackColor = System.Drawing.SystemColors.GradientActiveCaption;
            this.usernameBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.usernameBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.25F);
            this.usernameBox.ForeColor = System.Drawing.Color.SlateGray;
            this.usernameBox.Location = new System.Drawing.Point(119, 202);
            this.usernameBox.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.usernameBox.Name = "usernameBox";
            this.usernameBox.Size = new System.Drawing.Size(235, 25);
            this.usernameBox.TabIndex = 7;
            // 
            // passBox
            // 
            this.passBox.BackColor = System.Drawing.SystemColors.GradientActiveCaption;
            this.passBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.passBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.25F);
            this.passBox.ForeColor = System.Drawing.Color.SlateGray;
            this.passBox.Location = new System.Drawing.Point(119, 267);
            this.passBox.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.passBox.Name = "passBox";
            this.passBox.Size = new System.Drawing.Size(235, 25);
            this.passBox.TabIndex = 8;
            // 
            // SignupMedical
            // 
            this.SignupMedical.AutoSize = true;
            this.SignupMedical.Font = new System.Drawing.Font("Britannic Bold", 13.25F);
            this.SignupMedical.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.SignupMedical.LinkColor = System.Drawing.Color.SlateGray;
            this.SignupMedical.Location = new System.Drawing.Point(74, 465);
            this.SignupMedical.Name = "SignupMedical";
            this.SignupMedical.Size = new System.Drawing.Size(272, 26);
            this.SignupMedical.TabIndex = 11;
            this.SignupMedical.TabStop = true;
            this.SignupMedical.Text = "Sign up as medical center";
            this.SignupMedical.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLabel1_LinkClicked);
            // 
            // CheckRoles
            // 
            this.CheckRoles.BackColor = System.Drawing.SystemColors.GradientActiveCaption;
            this.CheckRoles.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.CheckRoles.CheckOnClick = true;
            this.CheckRoles.Font = new System.Drawing.Font("Britannic Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.CheckRoles.ForeColor = System.Drawing.Color.DimGray;
            this.CheckRoles.FormattingEnabled = true;
            this.CheckRoles.Items.AddRange(new object[] {
            "Medical center",
            "User"});
            this.CheckRoles.Location = new System.Drawing.Point(63, 327);
            this.CheckRoles.Margin = new System.Windows.Forms.Padding(4);
            this.CheckRoles.MultiColumn = true;
            this.CheckRoles.Name = "CheckRoles";
            this.CheckRoles.Size = new System.Drawing.Size(169, 75);
            this.CheckRoles.TabIndex = 16;
            this.CheckRoles.SelectedIndexChanged += new System.EventHandler(this.checkedListBox1_SelectedIndexChanged_1);
            // 
            // textBox3
            // 
            this.textBox3.BackColor = System.Drawing.SystemColors.GradientActiveCaption;
            this.textBox3.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.textBox3.Enabled = false;
            this.textBox3.Font = new System.Drawing.Font("Britannic Bold", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBox3.ForeColor = System.Drawing.SystemColors.MenuHighlight;
            this.textBox3.Location = new System.Drawing.Point(13, 503);
            this.textBox3.Margin = new System.Windows.Forms.Padding(4);
            this.textBox3.Multiline = true;
            this.textBox3.Name = "textBox3";
            this.textBox3.Size = new System.Drawing.Size(380, 61);
            this.textBox3.TabIndex = 17;
            this.textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // SignupUser
            // 
            this.SignupUser.AutoSize = true;
            this.SignupUser.Font = new System.Drawing.Font("Britannic Bold", 13.25F);
            this.SignupUser.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.SignupUser.LinkColor = System.Drawing.Color.SlateGray;
            this.SignupUser.Location = new System.Drawing.Point(123, 440);
            this.SignupUser.Name = "SignupUser";
            this.SignupUser.Size = new System.Drawing.Size(170, 26);
            this.SignupUser.TabIndex = 18;
            this.SignupUser.TabStop = true;
            this.SignupUser.Text = "Sign up as user";
            this.SignupUser.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLabel2_LinkClicked);
            // 
            // ForgotPassword
            // 
            this.ForgotPassword.AutoSize = true;
            this.ForgotPassword.Font = new System.Drawing.Font("Britannic Bold", 13.25F);
            this.ForgotPassword.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.ForgotPassword.LinkColor = System.Drawing.Color.SlateGray;
            this.ForgotPassword.Location = new System.Drawing.Point(86, 387);
            this.ForgotPassword.Name = "ForgotPassword";
            this.ForgotPassword.Size = new System.Drawing.Size(243, 26);
            this.ForgotPassword.TabIndex = 19;
            this.ForgotPassword.TabStop = true;
            this.ForgotPassword.Text = "Password dimenticata?";
            this.ForgotPassword.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLabel3_LinkClicked);
            // 
            // Login
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.BackColor = System.Drawing.SystemColors.GradientActiveCaption;
            this.ClientSize = new System.Drawing.Size(425, 577);
            this.Controls.Add(this.ForgotPassword);
            this.Controls.Add(this.SignupUser);
            this.Controls.Add(this.textBox3);
            this.Controls.Add(this.CheckRoles);
            this.Controls.Add(this.SignupMedical);
            this.Controls.Add(this.passBox);
            this.Controls.Add(this.usernameBox);
            this.Controls.Add(this.Signin);
            this.Controls.Add(this.pictureBox3);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.pictureBox1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Name = "Login";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Login";
            this.Load += new System.EventHandler(this.Login_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.PictureBox pictureBox3;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Button Signin;
        private System.Windows.Forms.TextBox usernameBox;
        private System.Windows.Forms.TextBox passBox;
        private System.Windows.Forms.LinkLabel SignupMedical;
        private System.Windows.Forms.CheckedListBox CheckRoles;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.LinkLabel SignupUser;
        private System.Windows.Forms.LinkLabel ForgotPassword;
    }
}

