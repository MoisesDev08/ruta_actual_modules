class ConversionError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        pass
    pass

class SameFormatError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        pass
    pass

from typing import Literal
class Celsius:
    
    def __init__(self, temp):
        self._temp = None
        self.temp = temp
        

    def _parser_from_str_to_temp(self, str):

        try:
            import re

            # parser sugerido por VS Code, no incluye mi razonamiento
            pattern = r"(-?\d+\.?\d*)\s*°?\s*([CFK])"
            match = re.match(pattern, str)

            if match:
                value, unit = match.groups()
                value = float(value)
                if unit == "C":
                    return value
                elif unit == "F":
                    return (value - 32) * 5/9
                elif unit == "K":
                    return value - 273.15
                
        except Exception as e:
            raise ConversionError(f"Error de parsing\nError: {e}\nError al convertir la cadena: {str}")
            
    @property
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self, value):
        if not isinstance(value, (int, float)):
            value = self._parser_from_str_to_temp(value)

        if isinstance(value, (int, float)):
            self._temp = value

    def _celcius_to_fahrenheit(self, temp):
        try:
            conversion = round((temp * (9/5)) + 32, 2)
            return conversion
        except ValueError:
            try:
                self._parser_from_str_to_temp(temp)
                conversion = round((self.temp * (9/5)) + 32, 2)
                return conversion
            except ConversionError:
                raise ConversionError(f"Error al convertir a Fahrenheit\nError: No se pudo convertir {temp} a un valor numérico")

    def _celcius_to_kelvin(self, temp):
        try:
            conversion = round((temp + 273.15), 2)
            return conversion
        except ValueError:
            try:
                self._parser_from_str_to_temp(temp)
                conversion = round((self.temp + 273.15), 2)
                return conversion
            except ConversionError:
                raise ConversionError(f"Error al convertir a Kelvin\nError: No se pudo convertir {temp} a un valor numérico")

    def convert_to(self, temp_obj: Literal["K", "F"], temp=None):
        try:

            if temp_obj == "C":
                raise SameFormatError("No se puede convertir temperaturas de °C a °C")
            
            if temp_obj == "K":
                if temp: return self._celcius_to_kelvin(temp)
                if not temp: return self._celcius_to_kelvin(self.temp)
            
            if temp_obj == "F":
                if temp: return self._celcius_to_fahrenheit(temp)
                if not temp: return self._celcius_to_fahrenheit(self.temp)

        except ValueError:
            raise ConversionError(f"Error al convertir\nError: No se pudo convertir {temp} a un valor numérico")

    def from_string(self, string):
        try:
            temper = self._parser_from_str_to_temp(string)
            return round(temper, 2)
        
        except ConversionError as e:
            raise ConversionError(f"Error al convertir desde string\nError: {e}")
    
    def value(self):
        return self.temp

    def __str__(self):
        return f"{self.temp} °C"

    def __repr__(self):
        return f"Celsius(self.temp={self.temp!r})"
class Fahrenheit:
    
    def __init__(self, temp):
        self._temp = None
        self.temp = temp
        
        pass

    def _parser_from_str_to_temp(self, str):
        try:
            import re

            # parser sugerido por VS Code, no incluye mi razonamiento
            pattern = r"(-?\d+\.?\d*)\s*°?\s*([CFK])"
            match = re.match(pattern, str)

            if match:
                value, unit = match.groups()
                value = float(value)
                if unit == "C":
                    return (value * 9/5) + 32
                elif unit == "F":
                    return value
                elif unit == "K":
                    return (value - 273.15) * 9/5 + 32
                
        except Exception as e:
            raise ConversionError(f"Error de parsing\nError: {e}\nError al convertir la cadena: {str}")

    @property
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self, value):
        if not isinstance(value, (int, float)):
            value = self._parser_from_str_to_temp(value)

        if isinstance(value, (int, float)):
            self._temp = value
        
    def convert_to(self, temp_obj: Literal["C", "K"], temp=None):
        try:

            if temp_obj == "F":
                raise SameFormatError("No se puede convertir temperaturas de °F a °F")
            
            if temp_obj == "C":
                if temp: return round((temp - 32) * 5/9, 2)
                if not temp: return round((self.temp - 32) * 5/9, 2)
            
            if temp_obj == "K":
                if temp: return round(((temp - 32) * 5/9) + 273.15, 2)
                if not temp: return round(((self.temp - 32) * 5/9) + 273.15, 2)

        except ValueError:
            raise ConversionError(f"Error al convertir\nError: No se pudo convertir {temp} a un valor numérico")
        

    def from_string(self, string):
        
        try:
            temper = self._parser_from_str_to_temp(string)
            return round(temper, 2)
        
        except ConversionError as e:
            raise ConversionError(f"Error al convertir desde string\nError: {e}")

    def value(self):
        return self.temp

    def __str__(self):
        return f"{self.temp} °F"

    def __repr__(self):
        return f"Fahrenheit(self.temp={self.temp!r})"
class Kelvin:
    
    def __init__(self, temp):
        self._temp = None
        self.temp = temp

    def _parser_from_str_to_temp(self, str):
        try:
            import re

            # parser sugerido por VS Code, no incluye mi razonamiento
            pattern = r"(-?\d+\.?\d*)\s*°?\s*([CFK])"
            match = re.match(pattern, str)

            if match:
                value, unit = match.groups()
                value = float(value)
                if unit == "C":
                    return value + 273.15
                elif unit == "F":
                    return ((value - 32) * 5/9) + 273.15
                elif unit == "K":
                    return value
                
        except Exception as e:
            raise ConversionError(f"Error de parsing\nError: {e}\nError al convertir la cadena: {str}")
    
    @property
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self, value):
        if not isinstance(value, (int, float)):
            value = self._parser_from_str_to_temp(value)

        if isinstance(value, (int, float)):
            self._temp = value

    def convert_to(self, temp_obj: Literal["C", "F"], temp=None):
        try:

            if temp_obj == "K":
                raise SameFormatError("No se puede convertir temperaturas de °K a °K")
            
            if temp_obj == "C":
                if temp: return round(temp - 273.15, 2)
                if not temp: return round(self.temp - 273.15, 2)
            
            if temp_obj == "F":
                if temp: return round(((temp - 273.15) * 9/5) + 32, 2)
                if not temp: return round(((self.temp - 273.15) * 9/5) + 32, 2)

        except ValueError:
            raise ConversionError(f"Error al convertir\nError: No se pudo convertir {temp} a un valor numérico")

    def from_string(self, string):
        try:
            temper = self._parser_from_str_to_temp(string)
            return round(temper, 2)
        
        except ConversionError as e:
            raise ConversionError(f"Error al convertir desde string\nError: {e}")
        
    def value(self):
        return self.temp

    def __str__(self):
        return f"{self.temp} °K"

    def __repr__(self):
        return f"Kelvin(self.temp={self.temp!r})"
    
centigrados = Celsius(25)
fahhrenheit = Fahrenheit(77)
kelvin = Kelvin(298.15)
temp_obj_list = [centigrados, fahhrenheit, kelvin]

def convert_temperature(unidad):
    import random
    for temp_obj in temp_obj_list:
        try:
            conversion = temp_obj.convert_to(unidad)
            print(f"Conversión de {temp_obj} a {unidad}: {conversion}")

            temp = random.randint(-100, 100)
            conversion = temp_obj.convert_to(unidad, temp)

            string = f"{random.randint(-100, 100)} °{unidad}"
            print(f"Valor de {temp_obj}: {temp_obj.value()} °{temp_obj.__str__()[-1]}")
            print(f"Parsing de str a temp: {string} -> {temp_obj.from_string(string)} °{temp_obj.__str__()[-1]}")
        except SameFormatError as e:
            print(f"Error: {e}")
        except ConversionError as e:
            print(f"Error: {e}")

unidades = ["C", "F", "K"]
for unidad in unidades:
    convert_temperature(unidad)



