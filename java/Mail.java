package com.work.hcq.jMail;

import java.util.Properties;

import javax.mail.MessagingException;
import javax.mail.internet.MimeMessage;

import org.springframework.mail.javamail.JavaMailSenderImpl;
import org.springframework.mail.javamail.MimeMessageHelper;

public class Mail {

	public  static void main(String[] args){

		JavaMailSenderImpl sender = new JavaMailSenderImpl();

		final String username = "479381142@qq.com";
		final String password = "ihmbgoezyuixcajg";
		
        sender.setHost("smtp.qq.com");
        sender.setPort(465);
        sender.setUsername(username);
        sender.setPassword(password); // 这里要用邀请码，不是你登录邮箱的密码

        Properties pro = System.getProperties(); // 下面各项缺一不可
        pro.put("mail.smtp.auth", "true");
        pro.put("mail.smtp.ssl.enable", "true");
        pro.put("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
        
        sender.setJavaMailProperties(pro);
  

        MimeMessage message = sender.createMimeMessage();
        try {
            MimeMessageHelper helper = new MimeMessageHelper(message, true,"UTF-8");
            helper.setTo("18883808948@163.com"); // 发送人 
            helper.setFrom("479381142@qq.com"); // 收件人  
            helper.setSubject("Title"); // 标题
           // helper.setText("Content"); // 内容
            helper.setText("<html><body><h1>JET!</h1>"
            		+ "<a href=http://www.baidu.com> </a> "
            		
            		+ "</body></html>",true);
            sender.send(message);
            System.out.println("发送完毕！");
        } catch (MessagingException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
	}
}
