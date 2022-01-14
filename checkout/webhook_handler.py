from django.http import HttpResponse


class stripeWH_handler:
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        handle a generic/unkown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )
    
    def handle_payment_intent_succeeded(self, event):
        """
        handle the payment_intent.succeeded webhook from stripe
        """
        return HttpResponse(
            content=f'webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        handle the payment_intent.payment_failed webhook from stripe
        """
        return HttpResponse(
            content=f'webhook received: {event["type"]}',
            status=200
        )
