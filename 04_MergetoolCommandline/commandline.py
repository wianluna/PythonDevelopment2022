import re

import cmd
from pynames import GENDER, LANGUAGE
from pynames.utils import get_all_generators
import shlex

GENDERS = {"female": GENDER.FEMALE, "male": GENDER.MALE}
LANGUAGES = {"en": LANGUAGE.EN, "ru": LANGUAGE.RU, "native": LANGUAGE.NATIVE}
GENERATORS = {}


def get_generators():
    elven_default = None
    iron_kingdoms_default = None
    generators = get_all_generators()
    for g in generators:
        generator_name = str(g)[:-2].split(".")[2:]
        race = generator_name[0].lower()
        subclass = re.sub(r"(Names|Fullname)*Generator", "", generator_name[1])
        if subclass.lower() == race:
            subclass = None
        GENERATORS[race, subclass] = g

        if race == "elven" and elven_default is None:
            elven_default = g
        if race == "iron_kingdoms" and iron_kingdoms_default is None:
            iron_kingdoms_default = g
    return elven_default, iron_kingdoms_default


class NameGenerator(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.language = LANGUAGE.NATIVE
        self.elven_default, self.iron_kingdoms_default = get_generators()

    def do_language(self, args):
        language = args.lower()
        if language not in LANGUAGE.ALL:
            language = LANGUAGES["native"]
        self.language = LANGUAGES[language]

    def create_generator(self, args):
        if len(args) == 1 and args[0] == "elven":
            generator = self.elven_default()
        elif len(args) == 1 and args[0] == "iron_kingdoms":
            generator = self.iron_kingdoms_default()
        elif len(args) == 1 or args[1].lower() in GENDERS or args[1] == "language":
            generator = GENERATORS[(args[0], None)]()
        else:
            generator = GENERATORS[(args[0], args[1])]()
        return generator

    def do_generate(self, args):
        args = shlex.split(args)
        generator = self.create_generator(args)

        if self.language not in generator.languages:
            language = LANGUAGES["native"]
        else:
            language = self.language

        if args[-1].lower() in GENDERS:
            print(generator.get_name_simple(GENDERS[args[-1].lower()], language))
        else:
            print(generator.get_name_simple(GENDERS["male"], language=language))

    def do_info(self, args):
        args = shlex.split(args)
        generator = self.create_generator(args)

        if args[-1] == "language":
            print(*generator.languages)
        elif args[-1].lower() in GENDERS:
            print(generator.get_names_number(GENDERS[args[-1].lower()]))
        else:
            print(generator.get_names_number())

    def do_bye(self, args):
        return True

    def do_exit(self, args):
        return True

    def do_quit(self, args):
        return True


if __name__ == "__main__":
    NameGenerator().cmdloop()
