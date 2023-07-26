from enum import Enum
from random import choice, randint


class SuperAbility(Enum):
    NONE = 0
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    BLOCK_DAMAGE_AND_REVERT = 4
    STUN_BOSS = 5
    REINCARNATION = 6
    KYS = 7
    KAMIKAZEBABAX = 8



class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = SuperAbility.NONE

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if hero.ability == SuperAbility.BLOCK_DAMAGE_AND_REVERT:
                    hero.blocked_damage = int(self.damage / 5)
                    hero.health -= int(self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence.name}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if isinstance(ability, SuperAbility):
            self.__ability = ability
        else:
            raise ValueError('Wrong data type for ability')

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass

    def __str__(self):
        return super().__str__() + f' ability: {self.__ability.name}'


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGEФ)

    def apply_super_power(self, boss, heroes):
        coeefccient = randint(2, 7)
        boss.health -= self.damage * coeefccient
        print(f'Warrior {self.name} hit critically {self.damage * coeefccient}')

class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)
        self.boost = random.randint(1, 10)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if isinstance(hero, Hero) and hero != self:
                hero.damage += self.boost_amount

    def apply_super_power(self, boss, heroes):
        self.apply_super_power(boss, heroes)


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.blocked_damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points



class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.STUN_BOSS)

    def apply_super_power(self, boss, heroes):
        stun_chance = random.random()
        if stun_chance < 0.3:  # 30% chance to stun the boss
            boss.stunned = True
            print(f'Thor stunned the boss.')
class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.HEAL)
    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            heroes.health += 900
class Bomber(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        if self.health <= 0:
            boss.health -= 100

class Boss(GameEntity):
    def attack(self, hero):
        if self.health > 0 and hero.health > 0:
            hero.health -= self.damage
            if hero.health <= 0 and isinstance(hero, Bomber):
                hero.explode(self)




round_number = 0


def show_stats(boss, heroes):
    print(f'ROUND {round_number} ----------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if boss.defence != hero.ability:
            hero.attack(boss)
            if hero.health > 0 and boss.health > 0:
                hero.apply_super_power(boss, heroes)
    show_stats(boss, heroes)


def start_game():
    boss = Boss('Doom', 1000, 50)

    warrior = Warrior('Superman', 270, 10)
    doc = Medic('Aibolit', 250, 5, 15)
    magic = Magic('Hendolf', 280, 15)
    berserk = Berserk('Garol', 260, 10)
    assistant = Medic('Haus', 300, 5, 5)
    magician = Magic



    heroes_list = [warrior, doc, magic, berserk, assistant]

    show_stats(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
