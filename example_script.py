import funzo_fact_gen as ffg

if __name__ == "__main__":
    fact_gen = ffg.FactGenerator()
    new_f = "y"
    while new_f == "y":
        print ""
        for fact in fact_gen.get_fact(count=5):
            print fact
        new_f = raw_input("\nMore facts? (y/n) ")
        while new_f not in ["y", "n"]:
            new_f = raw_input("Please enter either 'y' or 'n'. ")