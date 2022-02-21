from apscheduler.schedulers.blocking import BlockingScheduler
from decouple import config

from src.mail import send_mail

from .index import quidax

sched = BlockingScheduler()


def buy_crypto():
    try:
        markets = ["btc/ngn", "trx/ngn"]

        for asset in markets:

            crypto_asset, currency = asset.split("/")

            response = quidax.instant_orders.create_instant_order(
                "me",
                bid=currency,
                ask=crypto_asset,
                type="buy",
                total=10,
                unit=currency,
            )

            trade_id = response.get("data").get("id")

            confirmation = quidax.instant_orders.confirm_instant_orders(
                "me",
                trade_id,
            )

            buying_ngn = confirmation.get("data").get("total").get("amount")

            recieving_btc = confirmation.get("data").get("receive").get("amount")

            message = f"My comrade, we just bought {crypto_asset.upper()}{recieving_btc} with {currency.upper()}{buying_ngn}. i am proud of you buddy.\n 🚀🚀🚀🚀🚀🚀🚀🚀"

            send_mail(
                config("RECIEVING_EMAIL"),
                f"Comrade bot: we bought {crypto_asset.upper()} 🚀🚀🚀🚀🤘🏿🤘🏿🤘🏿🤘🏿🚀🚀🚀🚀.",
                message,
            )
    except Exception as e:
        send_mail(
            config("RECIEVING_EMAIL"),
            "Issue: Quidax has gintered my eyes ooo.",
            str(e),
        )

sched.add_job(
    buy_crypto,
    "cron",
    day_of_week="mon-sun",
    hour="13",
    minute="57",
    timezone="Africa/Lagos",
)

sched.start()
