#汉诺塔问题
#将n个盘子从A柱子移动到C柱子，B柱子作为辅助
#递归思想
#1.将n-1个盘子从A移动到B，C作为辅助
#2.将第n个盘子从A移动到C
#3.将n-1个盘子从B移动到C，A作为辅助
#递归结束条件：只有一个盘子

def move_tower(height, from_, with_, to_):
    if height >= 1:
        move_tower(height-1, from_, to_, with_)
        move_dish(from_, to_)
        move_tower(height-1, with_, from_, to_)
def move_dish(from_, to_):
    print(f"Move dish from {from_} to {to_}")
    
move_tower(3, "A", "B", "C")