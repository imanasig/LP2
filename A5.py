#Develop an elementary chatbot for any suitable customer interaction application.

def chatbot():

    print(" Welcome to SmartShop Assistant!")
    print("You can ask about products, price, order, delivery, payment, return")
    print("Type 'exit' to quit\n")

    # Knowledge Base (Facts)
    knowledge_base = {
        "greeting": ["hello", "hi", "hey"],
        "products": ["product", "items", "sell"],
        "price": ["price", "cost", "rate"],
        "order": ["order", "status"],
        "delivery": ["delivery", "shipping"],
        "payment": ["payment", "pay"],
        "return": ["return", "refund"],
        "thanks": ["thank"]
    }

    # Rule Base (Responses)
    responses = {
        "greeting": "Hello! How can I assist you today?",
        "products": "We offer electronics, clothing, shoes, and accessories.",
        "price": "Prices vary depending on the product. Please specify item.",
        "order": "Please enter your Order ID:",
        "delivery": "Delivery takes 3-5 business days.",
        "payment": "We accept Debit Card, Credit Card, UPI, and Net Banking.",
        "return": "Products can be returned within 7 days of delivery.",
        "thanks": "You're welcome!"
    }

    # Inference Engine
    def infer(user_input):
        matched_intents = {}

        for intent in knowledge_base:
            count = 0
            for word in knowledge_base[intent]:
                if word in user_input:
                    count += 1

            if count > 0:
                matched_intents[intent] = count

        # Select best match (highest score)
        if matched_intents:
            best_intent = max(matched_intents, key=matched_intents.get)
            confidence = matched_intents[best_intent]
            return best_intent, confidence

        return "unknown", 0

    # Chat Loop
    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "exit":
            print("Bot: Thank you for visiting SmartShop!")
            break

        intent, confidence = infer(user_input)

        if intent == "order":
            order_id = input("Bot: " + responses[intent] + " ")
            print("Bot: Order", order_id, "is being processed.")

        elif intent in responses:
            print("Bot:", responses[intent])

        else:
            print("Bot: Sorry, I didn't understand. Try again.")

chatbot()
