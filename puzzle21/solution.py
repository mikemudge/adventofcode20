def parseFood(lines):
    result = []
    for line in lines:
        print(line)

        ingredients, allergens = line.split(" (contains ")
        allergens = allergens[:-1].split(", ")
        ingredients = ingredients.split(" ")

        result.append((ingredients, allergens))
    return result


def part1():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        foodList = parseFood(lines)

        allergenMap = {}
        allIngredients = {}
        for food in foodList:
            print(food)
            ingredients, allergens = food
            for i in ingredients:
                if i not in allIngredients:
                    allIngredients[i] = []
                allIngredients[i].append(food)
            for a in allergens:
                if a not in allergenMap:
                    allergenMap[a] = []
                allergenMap[a].append(food)

        # Init all ingredients as free of allergens.
        allergenIngredients = {k: False for k in allIngredients}

        for a in allergenMap:
            print("Allergen %s" % a)
            foods = allergenMap[a]
            result = set(foods[0][0])
            for f in foods:
                result &= set(f[0])

            for possibleallergen in result:
                allergenIngredients[possibleallergen] = True

            print("possible ingredients which could contain %s" % a, result)

        r = 0
        for i in allergenIngredients:
            if allergenIngredients[i] is False:
                foodItemsContaining = len(allIngredients[i])
                print(i, allergenIngredients[i], "in", foodItemsContaining, "food items")
                r += foodItemsContaining

        print("Part 1:", r)


def part2():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        foodList = parseFood(lines)

        allergenMap = {}
        allIngredients = {}
        for food in foodList:
            print(food)
            ingredients, allergens = food
            for i in ingredients:
                if i not in allIngredients:
                    allIngredients[i] = []
                allIngredients[i].append(food)
            for a in allergens:
                if a not in allergenMap:
                    allergenMap[a] = []
                allergenMap[a].append(food)

        foodMap = {}
        for a in allergenMap:
            foods = allergenMap[a]
            result = set(foods[0][0])
            for f in foods:
                result &= set(f[0])

            foodMap[a] = list(result)
            print("possible ingredients which could contain %s" % a, result)

        print(foodMap)

        result = {}
        while len(foodMap) > 0:
            for f in foodMap:
                if len(foodMap[f]) == 1:
                    ingredient = foodMap[f][0]
                    print("%s must be in %s" % (f, ingredient))
                    result[f] = ingredient
                    foodMap.pop(f)
                    for f in foodMap:
                        if ingredient in foodMap[f]:
                            foodMap[f].remove(ingredient)
                    break
            print(foodMap)

        result = [result[key] for key in sorted(result)]
        print(result)
        print("Part 2:", ",".join(result))


part1()
part2()
