# Implementacija-neuronske-mreze-na-FPGA
Implementacija neuronske mreze na FPGA
## O projektu
Ovaj projekat demonstrira implementaciju jednostavne neuronske mreže na FPGA ploči kako bi se prepoznale ručno napisane cifre.
Model vestake inteligencije je obucen na MNIST dataset-u pomocu backpropagation algoritma. Mreza kao ulaz prihvata vektor od 784 neurona gde svaki neuron odgovara intenzitetu piksela slike rezolucije 28px. Mreza poseduje jedan nevidljivi sloj od 20 neurona i izlazni sloj od 10 neurona. Model koristi sigmoidnu aktivacionu funkciju.


![tikz12](https://github.com/vuklazovic/Implementacija-neuronske-mreze-na-FPGA/assets/68462413/4a32d0e8-555d-4334-a3aa-952e0027fbd5)

## Testiranje

Pomocu python scripte treba pripremiti sliku za predikciju komandom :
```python
cd python
python prepare_image.py <putanja do slike>
#reg signed [31:0] img [0:783] = '{0,0,0...0,0,0,0};
```
izlaz ove skripte treba kopirati u source.v verilog fajl.
Nakon generisanja bitstreama i pokretanja koda, uredjaj ce prediktovati broj i prikazati njegovu binarnu reprezentaciju pomocu led dioda.

## Ilustracija
![ilustration](https://github.com/vuklazovic/Implementacija-neuronske-mreze-na-FPGA/assets/68462413/06c9b8fa-cf09-4c9c-961a-8089d2cff99c)
