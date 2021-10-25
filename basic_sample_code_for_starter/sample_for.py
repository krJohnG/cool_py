#-*- coding:utf-8 -*-

# loop 5 time(height)
print('- loop 5 time(height)')
for count in range(5):
    print('*')
print('')

# loop 5 time(width)
print('- loop 5 time(width)')
for count in range(5):
    print('*', end='')

print('')
print('')

# triangle star
print('- triangle star')
for count_h in range(10):
    for count_w in range(count_h + 1):
        print('*', end=' ')
    print('')
print('')

# triangle star (reverse)
print('- triangle star (reverse)')
for count_h in reversed(range(10)):
    for count_w in range(count_h + 1):
        print('*', end=' ')
    print('')

# End