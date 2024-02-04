def age_assignment(*words, **kwords):
    result = []

    for k,v in kwords.items():
        for w in words:
            if w.startswith(k):
                result.append(f"{w} is {v} years old.")
    return "\n".join(sorted(result))

print(age_assignment("Amy", "Bill", "Willy", W=36,A=22, B=61))