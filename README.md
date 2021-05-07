# SMS-API
Sending out mass text messages using textbelt.us API

Following information taken from textbelt.com
Send and receive SMS with a clean, simple API
Textbelt is a no-nonsense SMS API built for developers who just want to send SMS. Thousands of customers prefer Textbelt over other SMS providers for our ease of setup, simple, predictable pricing packages, and personal support.

Using the Textbelt API
Textbelt is a simple API. The best way to get started is to try it yourself, or view the documentation here.

Here's an example success response after sending an SMS:

{"success": true, "quotaRemaining": 40, "textId": 12345}
Example out-of-quota or invalid key response:

{"success": false, "quotaRemaining": 0, "error": "Out of quota"}
Example response to request with phone, message, or key missing:

{"success": false, "error": "Incomplete request"}
Look up text delivery status
Using the textId given by a successful sent text, load /status/<textId>. For example, if your textId is 12345:

$ curl https://textbelt.com/status/12345

{"status": "DELIVERED"}
Possible return values include DELIVERED (carrier has confirmed sending), SENT (sent to carrier but confirmation receipt not available), SENDING (queued or dispatched to carrier), FAILED (not received), and UNKNOWN (could not determine status).

Delivery statuses are not standardized between mobile carriers. For example, some carriers will report SMS as "delivered" when they attempt transmission to the handset while other carriers actually report delivery receipts from the handsets.

Receiving SMS replies
U.S. phone numbers only: Textbelt lets you receive replies after you've sent an SMS. Replies are sent by webhook, meaning you will have to set up an HTTP or HTTPS route on your website that will process inbound SMS.

Add a replyWebhookUrl parameter to your HTTP request. For example:

$ curl -X POST https://textbelt.com/text \
    --data-urlencode phone='5555555555' \
    --data-urlencode message='Hello?' \
    -d replyWebhookUrl='https://my.site/api/handleSmsReply' \
    -d key=textbelt
Textbelt will POST the following JSON to your endpoint (in this case https://my.site/api/handleSmsReply):

{
  "fromNumber": "+1555123456",
  "text": "Here is my reply"
}
Read more for another example.

Checking your quota
Use /quota/<key> to view remaining quota. For example, if your key is abc123:

$ curl https://textbelt.com/quota/abc123

{"success": true, "quotaRemaining": 98}
Testing your key
If you want to validate your key without actually using your text quota, append "_test" to your key and you will receive a response from the /text endpoint confirming that a text would send, but it will not consume your credits.
