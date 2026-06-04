import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, EMAIL_TO, SITE_NAME


def send_email(subject: str, body_html: str, reply_to: str = None) -> bool:
    """Отправляет письмо на EMAIL_TO. Возвращает True при успехе."""
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"[{SITE_NAME}] {subject}"
        msg["From"] = f"{SITE_NAME} <{SMTP_USER}>"
        msg["To"] = EMAIL_TO
        if reply_to:
            msg["Reply-To"] = reply_to

        msg.attach(MIMEText(body_html, "html", "utf-8"))

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, EMAIL_TO, msg.as_string())
        return True
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")
        return False


def email_contact(name: str, email: str, phone: str, topic: str, message: str) -> bool:
    subject = f"Новая заявка: {topic}"
    body = f"""
    <html><body style="font-family:Arial,sans-serif;color:#222;">
      <h2 style="color:#1a3d1e;">Новая заявка с сайта</h2>
      <table style="border-collapse:collapse;width:100%;max-width:600px;">
        <tr><td style="padding:8px;background:#f5f5f5;font-weight:bold;width:140px;">Имя</td>
            <td style="padding:8px;border-bottom:1px solid #eee;">{name}</td></tr>
        <tr><td style="padding:8px;background:#f5f5f5;font-weight:bold;">Email</td>
            <td style="padding:8px;border-bottom:1px solid #eee;"><a href="mailto:{email}">{email}</a></td></tr>
        <tr><td style="padding:8px;background:#f5f5f5;font-weight:bold;">Телефон</td>
            <td style="padding:8px;border-bottom:1px solid #eee;">{phone or '—'}</td></tr>
        <tr><td style="padding:8px;background:#f5f5f5;font-weight:bold;">Тема</td>
            <td style="padding:8px;border-bottom:1px solid #eee;">{topic}</td></tr>
        <tr><td style="padding:8px;background:#f5f5f5;font-weight:bold;vertical-align:top;">Сообщение</td>
            <td style="padding:8px;">{message}</td></tr>
      </table>
    </body></html>
    """
    return send_email(subject, body, reply_to=email)


def email_vacancy(name: str, email: str, phone: str, position: str, message: str) -> bool:
    subject = f"Отклик на вакансию: {position}"
    body = f"""
    <html><body style="font-family:Arial,sans-serif;color:#222;">
      <h2 style="color:#1a3d1e;">Отклик на вакансию</h2>
      <table style="border-collapse:collapse;width:100%;max-width:600px;">
        <tr><td style="padding:8px;background:#f5f5f5;font-weight:bold;width:140px;">Имя</td>
            <td style="padding:8px;border-bottom:1px solid #eee;">{name}</td></tr>
        <tr><td style="padding:8px;background:#f5f5f5;font-weight:bold;">Email</td>
            <td style="padding:8px;border-bottom:1px solid #eee;"><a href="mailto:{email}">{email}</a></td></tr>
        <tr><td style="padding:8px;background:#f5f5f5;font-weight:bold;">Телефон</td>
            <td style="padding:8px;border-bottom:1px solid #eee;">{phone or '—'}</td></tr>
        <tr><td style="padding:8px;background:#f5f5f5;font-weight:bold;">Вакансия</td>
            <td style="padding:8px;border-bottom:1px solid #eee;">{position}</td></tr>
        <tr><td style="padding:8px;background:#f5f5f5;font-weight:bold;vertical-align:top;">О себе</td>
            <td style="padding:8px;">{message or '—'}</td></tr>
      </table>
    </body></html>
    """
    return send_email(subject, body, reply_to=email)
