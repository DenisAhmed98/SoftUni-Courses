line = input().split("|")  # прочитаме реда, като го разделяме по черта

sub_lists = []  # създаваме списък, в които ще пазим резултата

for sub_string in line[::-1]:  # развъртаме цикъл, който обхожда всеки подтекст в инпута
    sub_lists.extend(sub_string.split())
    # удължаваме списъка с резултата със списък от числата от конзолата, след като сме махнали всички спейсове

print(*sub_lists)