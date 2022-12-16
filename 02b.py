rock = 1
paper = 2
scissors = 3
lose = 0
draw = 3
win = 6

score = { 'A': {'X': scissors+lose, 'Y': rock+draw, 'Z': paper+win},
          'B': {'X': rock+lose, 'Y': paper+draw, 'Z': scissors+win},
          'C': {'X': paper+lose, 'Y': scissors+draw, 'Z': rock+win}}

total_score = 0
try:
    input_file = open("02.txt")
    for line in input_file:
        total_score += score[line[:1]][line[2]]
finally:
    input_file.close()
    print('Total score ',total_score)