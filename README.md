# 🧠 Brian2 Spiking Neural Network Simulation  

## Overview  
I have created a project in order to simulate a **Spiking Neural Network (SNN)** using **Brian2**, modeling simple **Leaky Integrate-and-Fire (LIF) neurons**.  
It visualizes membrane potential changes and generates a spike raster plot.  
This project is a Spiking Neural Network (SNN) Simulation using Brian2, which models how neurons fire and interact. It is based on the Leaky Integrate-and-Fire (LIF) neuron model and shows the firing pattern of neurons in a simple network.

I have been very interested in AI and neuroscience for the last two years. I have also read research papers on neural simulations, and I was very impressed by the Brian2Wasp browser, which allows real-time neural simulation. Coming from a biology teaching background and having a strong network of doctors, I have gained deep insights into neuroscience. Now, I am exploring how AI can be applied in this field to create useful solutions.

This is just a starting project, but I aim to work on more advanced AI-based neuroscience models in the future.

📌 Features
✅ Leaky Integrate-and-Fire (LIF) neuron model
✅ Simulation of multiple connected neurons
✅ Membrane potential and spike raster plot visualization
✅ Uses Brian2 for neural simulation
✅ Simple and easy to modify for further research

🎯 Installation
To run the simulation on your system, follow these steps:

1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/anshumandas04/brian2_snn_simulation.git
cd brian2_snn_simulation
2️⃣ Install dependencies
Make sure Python is installed, then run:
pip install -r requirements.txt


3️⃣ Run the simulation
python main.py
This will generate membrane potential graphs and a spike raster plot.

📊 How the Simulation Works
This simulation consists of 10 neurons, which are modeled as Leaky Integrate-and-Fire (LIF) neurons. 
Each neuron:

Receives an input current (I) that influences its membrane potential (V).
Fires a spike when its voltage crosses -50mV.
Resets to -65mV after firing.
Produces a raster plot showing which neurons fired and when.


🔬 Why LIF Neurons?
This is one of the most basic models of neurons, used in computational neuroscience to understand how real neurons behave. The LIF model is useful for simulating spiking activity in the brain and is a step toward more advanced brain-inspired AI.

📌 Expected Output
After running the code, you should see two plots:

1️⃣ Membrane Potential Graph – shows how voltage changes over time.
2️⃣ Spike Raster Plot – shows when and which neurons fired.



Dependencies:
The project requires the following Python libraries:

brian2
numpy
matplotlib

you can install them with:
pip install -r requirements.txt


🔬 Research Papers & References
I have referred to the following research papers and tools:

[Brian2Wasp: A Web-based Interface for Brian2 Simulations
Understanding Spiking Neural Networks](https://arxiv.org/abs/2301.10571)
https://arxiv.org/abs/1812.07040
https://brian2.readthedocs.io/en/stable/
I want to continue exploring how AI can be combined with neuroscience for more brain-inspired intelligence models.





🤝 Future Plans
This is my first neuroscience simulation project, and I want to take it further by:

Adding more complex neuron models like Hodgkin-Huxley.
Simulating real brain-like activity using AI techniques.
Collaborating with researchers who work in AI-based neuroscience.
If you are working in this field, feel free to reach out! 🚀
