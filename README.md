# Implementacija-neuronske-mreze-na-FPGA
Implementacija neuronske mreze na FPGA
## O projektu
Ovaj projekat demonstrira implementaciju jednostavne neuronske mreže na FPGA ploči kako bi se prepoznale ručno napisane cifre.
Model vestake inteligencije je obucen na MNIST dataset-u pomocu backpropagation algoritma. Mreza kao ulaz prihvata vektor od 784 neurona gde svaki neuron odgovara intenzitetu piksela slike rezolucije 28px. Mreza poseduje jedan nevidljivi sloj od 20 neurona i izlazni sloj od 10 neurona. Model koristi sigmoidnu aktivacionu funkciju.

![tikz12](https://github.com/vuklazovic/Implementacija-neuronske-mreze-na-FPGA/assets/68462413/5dd9551b-eca7-4626-add8-ad8882bed8f0)
