rock = 1
paper = 2
scissors = 3
loss = 0
draw = 3
win = 6

score = { 'A': {'X': rock+draw, 'Y': paper+win, 'Z': scissors+loss},
          'B': {'X': rock+loss, 'Y': paper+draw, 'Z': scissors+win},
          'C': {'X': rock+win, 'Y': paper+loss, 'Z': scissors+draw}}

total_score = 0
try:
    input_file = open("02.txt")
    for line in input_file:
        total_score += score[line[:1]][line[2]]
finally:
    input_file.close()
    print('Total score ',total_score)