def transfer(melody):
    if "A#" in melody:  
        melody = melody.replace("A#","a")
    if "C#" in melody:  
        melody = melody.replace("C#","c")
    if "D#" in melody:  
        melody = melody.replace("D#","d")
    if "F#" in melody:  
        melody = melody.replace("F#","f")
    if "G#" in melody:  
        melody = melody.replace("G#","g")
        
    return melody

def solution(m, musicinfos):
    
    m = transfer(m)
    answer = ""
    # 여러개일 때 재생시간이 가장 긴곡을 골라내기 위한 변수
    listen_melody_time = 0
    
    for music in musicinfos:
        start, end, name, melody = music.split(",")

        start_s , start_e = start.split(":")
        end_s , end_e = end.split(":")
        
        #음악이 재생된 시간
        time = 60 * (int(end_s) - int(start_s)) + (int(end_e)- int(start_e))
        
        #샾이 붙은 문자를 소문자로 변환
        melody = transfer(melody)
        
        listen_melody = melody * (time // len(melody)) + melody[:time % len(melody)]
        
        # 멜로디를 찾았으면 answer에 값을 저장하고 break
        if m in listen_melody:
            if(listen_melody_time < time):
                listen_melody_time = time
                answer = name

    if answer == "":
        return "(None)"    
    return answer
