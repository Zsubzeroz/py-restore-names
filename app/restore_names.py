from typing import List, Dict, Any


def restore_names(users: List[Dict[str, Any]]) -> None:
    for user in users:
        # 1. Verifica se 'first_name' está ausente ou é None
        if user.get("first_name") is None:
            full_name = user.get("full_name")

            # 2. Verifica se 'full_name' existe e é uma string (evita AttributeError e KeyError)
            if isinstance(full_name, str):
                # 3. Divide a string por espaços em branco
                parts = full_name.split()

                # 4. Verifica se a lista resultante não está vazia (evita IndexError)
                if parts:
                    user["first_name"] = parts[0]
