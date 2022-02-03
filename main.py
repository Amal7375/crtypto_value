import price
import emergencyNotification


while True:
    values=price.Value()

    message=emergencyNotification.telegramMessage(values)
