# for reading audio_analysis.txt
# pass in file path 
# returns list of audio_analysis dictionaries of string keys and values

def read_audio_analysiss(filename): 
    infile = open(filename, "r")
    data = infile.readlines()
    infile.close()
    audio_analysis = []

    for i in range(2): 
        elements = data[i].split("|")
        audio_analysis = dict() 
        audio_analysis["mode_confidence"] = elements[0]
        audio_analysis["end_of_fade_in"] = elements[1]
        audio_analysis["key_confidence"] = elements[2]
        audio_analysis["synch_version"] = elements[3]
        audio_analysis["duration"] = elements[4]
        audio_analysis["rhythm_version"] = elements[5]
        audio_analysis["time_signature_confidence"] = elements[6]
        audio_analysis["start_of_fade_out"] = elements[7]
        audio_analysis["analysis_sample_rate"] = elements[8]
        audio_analysis["tempo"] = elements[9]
        audio_analysis["offset_seconds"] = elements[10]
        audio_analysis["tempo_confidence"] = elements[11]
        audio_analysis["key"] = elements[12]
        audio_analysis["mode"] = elements[13]
        audio_analysis["time_signature"] = elements[14]
        audio_analysis["num_samples"] = elements[15]
        audio_analysis["loudness"] = elements[16]


        analysis["track"]["mode_confidence"],
        analysis["track"]["end_of_fade_in"],
        analysis["track"]["key_confidence"],
        analysis["track"]["synch_version"],
        analysis["track"]["duration"],
        analysis["track"]["rhythm_version"],
        analysis["track"]["time_signature_confidence"],
        analysis["track"]["start_of_fade_out"],
        analysis["track"]["analysis_sample_rate"],
        analysis["track"]["tempo"],
        analysis["track"]["offset_seconds"],
        analysis["track"]["tempo_confidence"],
        analysis["track"]["key"],
        analysis["track"]["mode"],
        analysis["track"]["time_signature"],
        analysis["track"]["num_samples"],
        analysis["track"]["loudness"]

        audio_analysis.append(audio_analysis) 

    return audio_analysis
        
    

