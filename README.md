¡Hola! Este es mi proyecto para la Actividad 1 de la materia de Programación Orientada a Objetos. Desarrollé un programa en Python que simula un entrenador Pokémon, donde apliqué conceptos como herencia, polimorfismo, redefinición de métodos y manejo de errores.

## 📌 ¿Qué hace este programa?
El sistema tiene un menú interactivo en consola que te permite:
- *Capturar Pokémon:* Crear Pokémon de tipo Fuego, Agua o Planta asignándoles sus estadísticas iniciales.
- *Entrenar Pokémon:* Subirles de nivel y aumentar sus puntos de ataque, defensa y salud.
- *Atacar:* Realizar combates entre dos Pokémon calculando el daño según su tipo (por ejemplo, Agua le hace el doble de daño a Fuego).
- *Ver información:* Consultar la lista y estadísticas de todos los Pokémon capturados.
- *Ver total:* Saber cuántos Pokémon tienes activos en tu equipo.
- *Liberar Pokémon:* Eliminar un Pokémon del equipo (activando su destructor).

## 🛠️ Conceptos de POO aplicados
- *Clase base y clases derivadas:* Creé una clase general Pokemon y tres subclases (PokemonFuego, PokemonAgua, PokemonPlanta).
- *Reutilización con super():* Usé super().__init__() para inicializar los atributos base y super().mostrar_info() para extender los mensajes de cada tipo.
- *Polimorfismo:* Redefiní el método atacar() en cada clase derivada para aplicar las ventajas y desventajas elementales.
- *Métodos de clase y estáticos:* Usé un @classmethod para contar los Pokémon creados y un @staticmethod para validar que las estadísticas ingresadas sean números positivos.
- *Manejo de excepciones:* Todo el menú está protegido con bloques try/except para evitar que el programa se cierre por un mal ingreso de datos.

## 🚀 ¿Cómo ejecutarlo?
Para probar el código solo necesitas tener instalado Python 3 y ejecutar
