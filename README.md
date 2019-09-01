# customize-chatbot
This is designed to teach you how to create simple deep learning chatbot using python, tensorflow and nltk. The chatbot we design will be used for a specific purpose like answering questions about a business.

You will learn and understand the following after this tutorial:

How a Neural Network Works

How to Design a Neural Network

How to Train a Neural Network

How to Create a Chatbot

How to Create a Chatbot Framework

How to Deploy a Chatbot

#LOADING DATA

Now it's time to understand what kind of data we will need to provide our chatbot with. Since this is a simple chatbot we don't need to download any massive datasets. We will just use data that we write ourselves. To follow along with the tutorial properly you will need to create a .JSON file that contains the same format as the one seen below. I've called my file "intents.json".
What we are doing with the JSON file is creating a bunch of messages that the user is likely to type in and mapping them to a group of appropriate responses. The tag on each dictionary in the file indicates the group that each message belongs too. With this data we will train a neural network to take a sentence of words and classify it as one of the tags in our file. Then we can simply take a response from those groups and display that to the user. The more tags, responses, and patterns you provide to the chatbot the better and more complex it will be.
