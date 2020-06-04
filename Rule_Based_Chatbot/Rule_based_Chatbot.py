from nltk.chat.util import Chat, reflections


chat_responses = [
  ['Hi|Hello|Hey','Hello'],
  ['Good (.*)','Good %1'],
  ['How are you', 'I am fine thank you, how are you?'],
  ['What is your name', 'My name is ULTRON'],
  ['Who (.*) you', 'I was designed by Mr. Saurav Sharma'],
  ['When were you (.*)','My development started on 10 May 2020 during the coronavirus'],
  ['Why were you made',' Mr. Sharma wanted to make me as he was free and needed someone to kill time with and as a result I was born'],
  ['What is your hobby', 'To respond to users such as you'],
  ['Are you a good chatbot', 'I am a work in progress as there is always scope for improvement'],
  ['(.*) help (.*)', 'I might be able to help you']
                    ]


chat=Chat(chat_responses, reflections)
chat.converse()
