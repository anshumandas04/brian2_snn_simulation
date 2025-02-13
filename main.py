import brian2 as b2
import matplotlib.pyplot as plt

# Simulation Parameters
b2.defaultclock.dt = 0.1 * b2.ms

# Define Leaky Integrate-and-Fire (LIF) Model Equations
eqs = '''
dv/dt = (-(v - v_rest) + I) / tau : volt
I : volt  # External input
tau : second
v_rest : volt
'''

# Create a Neuron Group
N = 10  # Number of neurons
neurons = b2.NeuronGroup(N, eqs, threshold='v > -50*mV', reset='v = v_rest', method='euler')

# Initialize Parameters
neurons.v = -65 * b2.mV
neurons.tau = 10 * b2.ms
neurons.v_rest = -65 * b2.mV
neurons.I = 15 * b2.mV  # External input current

# Monitor Spikes and Voltage
M = b2.StateMonitor(neurons, 'v', record=True)
S = b2.SpikeMonitor(neurons)

# Run Simulation
b2.run(100 * b2.ms)

# Plot Results
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(M.t / b2.ms, M.v[0] / b2.mV, label='Neuron 1')
plt.ylabel('Membrane Potential (mV)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(S.t / b2.ms, S.i, '.k')
plt.xlabel('Time (ms)')
plt.ylabel('Neuron Index')
plt.title('Spike Raster Plot')

plt.tight_layout()
plt.show()
