import math


class Pokemon:

    _contador_pokemons = 0

    def __init__(self, nombre: str, ataque: int, defensa: int, salud: int):
        if not self.validar_estadistica(ataque) or not self.validar_estadistica(defensa) or not self.validar_estadistica(salud):
            raise ValueError("Las estadísticas deben ser números enteros o decimales positivos.")
        
        self.nombre = nombre
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        self.salud_maxima = salud
        self._tipo = "Normal"
        
        Pokemon._contador_pokemons += 1
        print(f"¡{self.nombre} ha sido capturado! 🎉")

    def __del__(self):
        Pokemon._contador_pokemons -= 1
        print(f"✨ {self.nombre} ha sido liberado ✨")

    @classmethod
    def total_pokemons(cls):
        """Devuelve cuántos Pokémon han sido creados (activos)"""
        return cls._contador_pokemons

    @staticmethod
    def validar_estadistica(valor):
        """Verifica que un valor de estadística sea positivo."""
        return isinstance(valor, (int, float)) and valor > 0

    def subir_nivel(self):
        """Método interno que sube de nivel y mejora estadísticas base."""
        self.nivel += 1
        self.ataque += 2
        self.defensa += 2
        self.salud_maxima += 5
        self.salud = self.salud_maxima
        print(f"¡{self.nombre} ha subido al Nivel {self.nivel}! Sus stats han aumentado.")

    def entrenar(self, stat1=None, stat2=None, stat3=None):
        """Simula sobrecarga con parámetros opcionales por defecto."""
        self.subir_nivel()
        if stat1 is None and stat2 is None and stat3 is None:
            self.ataque += 3
            self.defensa += 3
            self.salud_maxima += 5
            self.salud = self.salud_maxima
            print(f"Entrenamiento general completo: Todas las estadísticas de {self.nombre} mejoraron extra.")
        else:
            stats = [stat1, stat2, stat3]
            for s in stats:
                if s == "ataque":
                    self.ataque += 5
                elif s == "defensa":
                    self.defensa += 5
                elif s == "salud":
                    self.salud_maxima += 10
                    self.salud = self.salud_maxima

    def recibir_dano(self, cantidad: int):
        self.salud -= cantidad
        if self.salud <= 0:
            self.salud = 0
            print(f"💀 ¡{self.nombre} se ha debilitado!")
        else:
            print(f"💥 {self.nombre} recibió {cantidad} de daño. Salud restante: {self.salud}/{self.salud_maxima}")

    def atacar(self, objetivo):
        dano_base = max(1, self.ataque - objetivo.defensa)
        print(f"⚔️ {self.nombre} ataca a {objetivo.nombre} infligiendo {dano_base} de daño base.")
        objetivo.recibir_dano(dano_base)

    def mostrar_info(self):
        print(f"\n--- 📋 {self.nombre} [{self._tipo}] ---")
        print(f"Nivel: {self.nivel} | Salud: {self.salud}/{self.salud_maxima}")
        print(f"Ataque: {self.ataque} | Defensa: {self.defensa}")


class PokemonFuego(Pokemon):
    def __init__(self, nombre: str, ataque: int, defensa: int, salud: int):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Fuego"

    def atacar(self, objetivo):
        dano_base = max(1, self.ataque - objetivo.defensa)
        multiplicador = 1.0
        
        if objetivo._tipo == "Planta":
            multiplicador = 2.0
            print("🔥 ¡Es súper efectivo! (+100% de daño)")
        elif objetivo._tipo == "Agua":
            multiplicador = 0.5
            print("🌊 No es muy efectivo... (-50% de daño)")

        dano_final = max(1, math.floor(dano_base * multiplicador))
        print(f"⚔️ {self.nombre} lanza un ataque de Fuego a {objetivo.nombre}!")
        objetivo.recibir_dano(dano_final)

    def mostrar_info(self):
        super().mostrar_info()
        print("🔥 ¡Arde con pasión!")


class PokemonAgua(Pokemon):
    def __init__(self, nombre: str, ataque: int, defensa: int, salud: int):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Agua"

    def atacar(self, objetivo):
        dano_base = max(1, self.ataque - objetivo.defensa)
        multiplicador = 1.0
        
        if objetivo._tipo == "Fuego":
            multiplicador = 2.0
            print("💧 ¡Es súper efectivo! (+100% de daño)")
        elif objetivo._tipo == "Planta":
            multiplicador = 0.5
            print("🌿 No es muy efectivo... (-50% de daño)")

        dano_final = max(1, math.floor(dano_base * multiplicador))
        print(f"⚔️ {self.nombre} lanza un ataque de Agua a {objetivo.nombre}!")
        objetivo.recibir_dano(dano_final)

    def mostrar_info(self):
        super().mostrar_info()
        print("💧 ¡Fluye como el río!")


class PokemonPlanta(Pokemon):
    def __init__(self, nombre: str, ataque: int, defensa: int, salud: int):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Planta"

    def atacar(self, objetivo):
        dano_base = max(1, self.ataque - objetivo.defensa)
        multiplicador = 1.0
        
        if objetivo._tipo == "Agua":
            multiplicador = 2.0
            print("🌿 ¡Es súper efectivo! (+100% de daño)")
        elif objetivo._tipo == "Fuego":
            multiplicador = 0.5
            print("🔥 No es muy efectivo... (-50% de daño)")

        dano_final = max(1, math.floor(dano_base * multiplicador))
        print(f"⚔️ {self.nombre} lanza un ataque de Planta a {objetivo.nombre}!")
        objetivo.recibir_dano(dano_final)

    def mostrar_info(self):
        super().mostrar_info()
        print("🌿 ¡Crece con fuerza!")


def mostrar_menu():
    print("\n========================================")
    print("      🎮 SIMULADOR POKÉMON - MENÚ      ")
    print("========================================")
    print("1. Capturar Pokémon")
    print("2. Entrenar Pokémon")
    print("3. Atacar")
    print("4. Consultar la información")
    print("5. Total de Pokémon creados")
    print("6. Liberar Pokémon")
    print("7. Salir")
    print("========================================")

def seleccionar_pokemon(equipo, mensaje):
    if not equipo:
        print("❌ No tienes Pokémon en tu equipo.")
        return None
    print(f"\n--- {mensaje} ---")
    for i, p in enumerate(equipo, 1):
        estado = " (Debilitado)" if p.salud == 0 else ""
        print(f"{i}. {p.nombre} [{p._tipo}] - Nivel {p.nivel} - PS: {p.salud}/{p.salud_maxima}{estado}")
    try:
        idx = int(input("Selecciona el número del Pokémon: ")) - 1
        if 0 <= idx < len(equipo):
            return equipo[idx]
        print("⚠️ Número fuera de rango.")
    except ValueError:
        print("⚠️ Debe ingresar un número entero válido.")
    return None

def main():
    equipo = []
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-7): ").strip()

        if opcion == "1":
            print("\n--- 🔴 CAPTURAR POKÉMON ---")
            nombre = input("Nombre del Pokémon: ").strip()
            if not nombre:
                print("❌ El nombre no puede estar vacío.")
                continue

            tipo = input("Tipo (Fuego/Agua/Planta): ").strip().capitalize()
            if tipo not in ["Fuego", "Agua", "Planta"]:
                print("❌ Tipo no permitido. Debe ser Fuego, Agua o Planta.")
                continue
                
            try:
                ataque = int(input("Puntos de Ataque (>0): "))
                defensa = int(input("Puntos de Defensa (>0): "))
                salud = int(input("Puntos de Salud (>0): "))

                if not (Pokemon.validar_estadistica(ataque) and Pokemon.validar_estadistica(defensa) and Pokemon.validar_estadistica(salud)):
                    print("❌ Las estadísticas deben ser números positivos mayores a 0.")
                    continue

                if tipo == "Fuego":
                    p = PokemonFuego(nombre, ataque, defensa, salud)
                elif tipo == "Agua":
                    p = PokemonAgua(nombre, ataque, defensa, salud)
                elif tipo == "Planta":
                    p = PokemonPlanta(nombre, ataque, defensa, salud)

                equipo.append(p)
            except ValueError as e:
                print(f"❌ Entrada inválida: {e}")

        elif opcion == "2":
            p = seleccionar_pokemon(equipo, "ENTRENAR POKÉMON")
            if p:
                modo = input("¿Deseas entrenamiento personalizado? (s/n): ").strip().lower()
                if modo == 's':
                    s1 = input("Stat principal a mejorar (ataque/defensa/salud): ").strip().lower()
                    p.entrenar(stat1=s1)
                else:
                    p.entrenar() 

        elif opcion == "3":
            if len(equipo) < 2:
                print("⚠️️ Necesitas al menos 2 Pokémon en tu equipo para simular una batalla.")
                continue
            print("\n--- ⚔️ BATALLA POKÉMON ---")
            atacante = seleccionar_pokemon(equipo, "Selecciona al Atacante")
            if not atacante:
                continue
            
            if atacante.salud <= 0:
                print("❌ Un Pokémon debilitado no puede atacar.")
                continue

            defensor = seleccionar_pokemon(equipo, "Selecciona al Objetivo")
            if not defensor:
                continue

            if atacante == defensor:
                print("❌ Un Pokémon no puede atacarse a sí mismo.")
                continue

            atacante.atacar(defensor)

        elif opcion == "4":
            if not equipo:
                print("ℹ️ Tu equipo está vacío.")
            else:
                print("\n--- 📋 EQUIPO POKÉMON ---")
                for p in equipo:
                    p.mostrar_info() 

        elif opcion == "5":
            print(f"\n📊 Total de Pokémon creados activos: {Pokemon.total_pokemons()}")

        elif opcion == "6":
            p = seleccionar_pokemon(equipo, "LIBERAR POKÉMON")
            if p:
                equipo.remove(p)
                del p  
        elif opcion == "7":
            print("\n¡Gracias por jugar, Maestro Pokémon! Hasta pronto. 👋")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()