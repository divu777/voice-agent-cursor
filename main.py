import speech_recognition as sr
from graph import compile_with_checkpointer, graph_builder,State
r = sr.Recognizer()
MONGODB_URL = 'mongodb://admin:admin@localhost:27017'
from langgraph.checkpoint.mongodb import MongoDBSaver


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source=source)
    r.pause_threshold=2

    print("Listening======");
    audio = r.listen(source=source)

    print("Processing=====")
    stt = r.recognize_google(audio)
    print("Output=======")
    print(stt)

    with MongoDBSaver.from_conn_string(MONGODB_URL) as checkpointer:

        graph = compile_with_checkpointer(checkpointer=checkpointer,graph_builder=graph_builder)

        config = {
            "configurable":{
                "thread_id":"540"
            }
        }

        _state:State={
            "messages":[{"role":"user","content":stt}]
        }


        for events in graph.stream(_state , config=config,stream_mode='values'):
            if 'messages' in events:
                events["messages"][-1].pretty_print()