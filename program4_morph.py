words=["unhappiness","replayed","international"]
morphemes={
    "unhappiness":[("un-","Bound morpheme"),("happy-","Free morpheme"),("ness-","Bound morpheme")],
    "replayed":[("re-","Bound morpheme"),("play-","Free morpheme"),("-ed","Bound morpheme")],
    "international":[("inter-","Bound morpheme"),("nation-","Free morpheme"),("-al","Bound morpheme")]
}
for word in words:
    print("Word:",word)
    print("Morphemes: ")
    for morpheme,morpheme_type in morphemes[word]:
        print(morpheme," ",morpheme_type)
