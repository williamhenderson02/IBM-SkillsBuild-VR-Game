using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Net;
using System.Net.Mail;

public class Email: MonoBehaviour
{
    public void SendMail()
    {
        MailAddress to = new MailAddress("tgpz35@durham.ac.uk");
        MailAddress from = new MailAddress("spaceescapevr@gmail.com");

        MailMessage email = new MailMessage(from, to);
        email.Subject = "IBM Skills Build Link";
        email.Body = "Welcome to VR Space Escape!\n\nTo access the IBM SkillsBuild content click this link to log in and review quiz content: https://skillsbuild.org/ \n\nIf you do not have an account follow the instructions in section 2.1 of the user manual if you're unsure about account creation and configuration!";

        SmtpClient smtp = new SmtpClient();
        smtp.Host = "smtp.gmail.com";
        smtp.Port = 25;
        smtp.Credentials = new NetworkCredential("spaceescapevr@gmail.com", "qgsycfeofeqajwmu");
        smtp.DeliveryMethod = SmtpDeliveryMethod.Network;
        smtp.EnableSsl = true;
        try
        {
            /* Send method called below is what will send off our email 
                * unless an exception is thrown.
                */
            smtp.Send(email);
        }
        catch (SmtpException ex)
        {
            Console.WriteLine(ex.ToString());
        }
    }
}