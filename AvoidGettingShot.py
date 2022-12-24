
def avoidGettingShot(k:int,n:int, people:list[int]) -> int:
    #Count the number of people been short
    peopleShot = 0

    #Loop over the people
    for i in range(0,n):

        # if height is Greater than shot them
        if people[i] > k:
            peopleShot += 1
    
    return peopleShot

if __name__ == "__main__":
    # Test Case
    numberOfPeople = [4, 5, 4]
    height = [10,8,6]
    peoples = [[2, 13, 4, 16],[9,3,8,8,4],[1,2,3,4]] 
    for i in range(3):
        print(f'Input -> numberOfPeople = {numberOfPeople[i]}, height = {height[i]}, peoples = {peoples[i]}')
        print(f'Output -> Number of people to be kill = {avoidGettingShot(height[i], numberOfPeople[i], peoples[i])}')