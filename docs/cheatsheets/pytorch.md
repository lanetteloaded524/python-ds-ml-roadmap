# PyTorch Cheat Sheet

> **Quick Reference** — `import torch` / `import torch.nn as nn`

---

## 📦 Tensor Creation

| Function | Description | Example |
|---|---|---|
| `torch.tensor()` | From Python data | `torch.tensor([1, 2, 3])` |
| `torch.zeros()` | All zeros | `torch.zeros(3, 4)` |
| `torch.ones()` | All ones | `torch.ones(2, 3)` |
| `torch.randn()` | Normal distribution | `torch.randn(3, 3)` |
| `torch.rand()` | Uniform [0, 1) | `torch.rand(2, 4)` |
| `torch.arange()` | Range with step | `torch.arange(0, 10, 2)` |
| `torch.linspace()` | Evenly spaced | `torch.linspace(0, 1, 5)` |
| `torch.eye()` | Identity matrix | `torch.eye(3)` |
| `torch.from_numpy()` | From NumPy array | `torch.from_numpy(np_array)` |
| `torch.empty()` | Uninitialized | `torch.empty(2, 3)` |
| `torch.full()` | Fill with value | `torch.full((2, 2), 7.0)` |
| `torch.zeros_like(x)` | Same shape as x | `torch.zeros_like(x)` |

---

## 🔍 Tensor Attributes

| Attribute | Description | Example Output |
|---|---|---|
| `x.shape` / `x.size()` | Dimensions | `torch.Size([3, 4])` |
| `x.dtype` | Data type | `torch.float32` |
| `x.device` | CPU or CUDA device | `device(type='cuda', index=0)` |
| `x.requires_grad` | Track gradients? | `True` / `False` |
| `x.ndim` | Number of dimensions | `2` |
| `x.numel()` | Total elements | `12` |

---

## ➕ Operations

### Arithmetic

```python
x + y          # element-wise add
x - y          # subtract
x * y          # element-wise multiply
x / y          # divide
x ** 2         # power
torch.sqrt(x)
torch.exp(x)
torch.log(x)
```

### Matrix Operations

```python
x @ y                    # matrix multiply
torch.matmul(x, y)      # same as @
torch.mm(x, y)          # 2D matrix multiply only
torch.bmm(x, y)         # batch matrix multiply (3D)
x.t()                   # transpose (2D only)
x.T                     # transpose
```

### Shape Manipulation

| Function | Description | Example |
|---|---|---|
| `x.reshape(r, c)` | Reshape (may copy) | `x.reshape(2, 6)` |
| `x.view(r, c)` | Reshape (view, contiguous only) | `x.view(2, -1)` |
| `x.squeeze()` | Remove size-1 dims | `x.squeeze(0)` |
| `x.unsqueeze(dim)` | Add dim at position | `x.unsqueeze(0)` — add batch dim |
| `torch.cat([a,b], dim)` | Concatenate along dim | `torch.cat([a, b], dim=0)` |
| `torch.stack([a,b], dim)` | Stack along new dim | `torch.stack([a, b], dim=0)` |
| `x.permute(dims)` | Reorder dimensions | `x.permute(2, 0, 1)` |
| `x.contiguous()` | Make memory contiguous | `x.permute(...).contiguous()` |
| `torch.clamp(x, min, max)` | Clamp values | `torch.clamp(x, 0, 1)` |
| `x.flatten()` | Flatten to 1D | `x.flatten()` |

---

## 🔄 Autograd

```python
x = torch.randn(3, requires_grad=True)
y = (x ** 2).sum()
y.backward()          # compute gradients
print(x.grad)         # dy/dx

# Stop tracking gradients
with torch.no_grad():
    y = model(x)      # inference, no gradient computation

# Detach from computation graph
z = x.detach()        # returns tensor without grad tracking

# Zero gradients (important in training loops)
optimizer.zero_grad()
```

---

## 💻 Device Management

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Move tensor to device
x = x.to(device)
x = x.cuda()    # to GPU
x = x.cpu()     # to CPU

# Move model to device
model = model.to(device)

# Create tensor on device directly
x = torch.randn(3, 3, device=device)

# Check GPU info
torch.cuda.device_count()
torch.cuda.get_device_name(0)
torch.cuda.memory_allocated()
```

---

## 🏗 nn.Module Pattern

```python
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = MyModel(784, 128, 10)
print(model)                                 # architecture summary
print(sum(p.numel() for p in model.parameters()))  # total params
```

---

## 🧱 Common Layers

| Layer | Description | Example |
|---|---|---|
| `nn.Linear(in, out)` | Fully connected | `nn.Linear(128, 64)` |
| `nn.Conv2d(in_ch, out_ch, k)` | 2D convolution | `nn.Conv2d(3, 16, 3, padding=1)` |
| `nn.MaxPool2d(k)` | Max pooling | `nn.MaxPool2d(2)` |
| `nn.AvgPool2d(k)` | Average pooling | `nn.AvgPool2d(2)` |
| `nn.BatchNorm1d(n)` | Batch norm (1D) | `nn.BatchNorm1d(64)` |
| `nn.BatchNorm2d(n)` | Batch norm (2D) | `nn.BatchNorm2d(16)` |
| `nn.Dropout(p)` | Dropout | `nn.Dropout(0.5)` |
| `nn.Embedding(vocab, dim)` | Embedding lookup | `nn.Embedding(10000, 300)` |
| `nn.LSTM(in, hid, layers)` | LSTM | `nn.LSTM(300, 128, num_layers=2, batch_first=True)` |
| `nn.GRU(in, hid, layers)` | GRU | `nn.GRU(300, 128, batch_first=True)` |
| `nn.TransformerEncoderLayer` | Transformer layer | `nn.TransformerEncoderLayer(d_model=512, nhead=8)` |

---

## ⚡ Activation Functions

| Activation | Description | Usage |
|---|---|---|
| `nn.ReLU()` | max(0, x) | Default for hidden layers |
| `nn.LeakyReLU(0.01)` | Leaky ReLU | Avoids dead neurons |
| `nn.GELU()` | Gaussian Error LU | Transformers |
| `nn.Sigmoid()` | σ(x) ∈ (0,1) | Binary output |
| `nn.Softmax(dim)` | Normalized probabilities | Multi-class output |
| `nn.Tanh()` | tanh(x) ∈ (-1,1) | RNNs, bounded output |
| `nn.SiLU()` | x·σ(x) (Swish) | Modern architectures |

---

## 📉 Loss Functions

| Loss | Use Case | Example |
|---|---|---|
| `nn.MSELoss()` | Regression | `nn.MSELoss()(pred, target)` |
| `nn.L1Loss()` | Regression (MAE) | `nn.L1Loss()(pred, target)` |
| `nn.CrossEntropyLoss()` | Multi-class (raw logits) | `nn.CrossEntropyLoss()(logits, labels)` |
| `nn.NLLLoss()` | Multi-class (log probs) | After `LogSoftmax` |
| `nn.BCELoss()` | Binary (after sigmoid) | `nn.BCELoss()(sigmoid_out, target)` |
| `nn.BCEWithLogitsLoss()` | Binary (raw logits) | More stable than BCE + Sigmoid |
| `nn.SmoothL1Loss()` | Robust regression | Huber loss |

> ⚠️ `CrossEntropyLoss` expects **raw logits** (no softmax) and **integer labels**.

---

## 🎯 Optimizers & Schedulers

```python
import torch.optim as optim

# Optimizers
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
optimizer = optim.Adam(model.parameters(), lr=1e-3)
optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)

# Learning rate schedulers
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=5)

# Call scheduler.step() after each epoch (or batch for some schedulers)
```

---

## 🔄 Training Loop Template

```python
model = MyModel(input_dim, hidden_dim, output_dim).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

num_epochs = 20
for epoch in range(num_epochs):
    # --- Training ---
    model.train()
    train_loss = 0.0
    for batch_x, batch_y in train_loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)

        optimizer.zero_grad()
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()

    # --- Validation ---
    model.eval()
    val_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_x, batch_y in val_loader:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)
            outputs = model(batch_x)
            loss = criterion(outputs, batch_y)
            val_loss += loss.item()

            _, predicted = outputs.max(1)
            total += batch_y.size(0)
            correct += predicted.eq(batch_y).sum().item()

    print(f"Epoch {epoch+1}/{num_epochs} | "
          f"Train Loss: {train_loss/len(train_loader):.4f} | "
          f"Val Loss: {val_loss/len(val_loader):.4f} | "
          f"Val Acc: {100.*correct/total:.2f}%")
```

---

## 📂 Data Loading

```python
from torch.utils.data import Dataset, DataLoader, TensorDataset

# Quick: TensorDataset
dataset = TensorDataset(torch.randn(1000, 10), torch.randint(0, 2, (1000,)))
loader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=2)

# Custom Dataset
class MyDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

dataset = MyDataset(X, y)
loader = DataLoader(dataset, batch_size=64, shuffle=True,
                    num_workers=4, pin_memory=True)
```

---

## 💾 Save & Load

```python
# Save model weights (recommended)
torch.save(model.state_dict(), 'model_weights.pth')

# Load model weights
model = MyModel(input_dim, hidden_dim, output_dim)
model.load_state_dict(torch.load('model_weights.pth'))
model.eval()

# Save entire model (less portable)
torch.save(model, 'full_model.pth')
model = torch.load('full_model.pth')

# Save checkpoint (for resuming training)
torch.save({
    'epoch': epoch,
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': loss,
}, 'checkpoint.pth')

# Load checkpoint
ckpt = torch.load('checkpoint.pth')
model.load_state_dict(ckpt['model_state_dict'])
optimizer.load_state_dict(ckpt['optimizer_state_dict'])
```

---

## 🛠 Useful Utilities

| Function / Pattern | Description |
|---|---|
| `torch.manual_seed(42)` | Set random seed for reproducibility |
| `torch.cuda.manual_seed_all(42)` | Seed all GPUs |
| `model.eval()` | Set eval mode (disables dropout/batchnorm updates) |
| `model.train()` | Set training mode |
| `torch.no_grad()` | Context manager — no gradient computation |
| `torch.inference_mode()` | Faster than `no_grad` for inference |
| `nn.utils.clip_grad_norm_(params, max)` | Gradient clipping |
| `torchsummary.summary(model, input_size)` | Model architecture summary |
| `x.numpy()` | Tensor → NumPy (CPU only) |
| `x.item()` | Single-element tensor → Python scalar |

---

## 💡 Quick Tips

1. **Always call `model.eval()`** before inference and `model.train()` before training — this toggles dropout and batchnorm behavior.
2. **Use `torch.no_grad()`** during validation/inference to save memory and speed up computation.
3. **Pin memory** in DataLoader (`pin_memory=True`) when training on GPU for faster data transfer.
4. **Don't forget `optimizer.zero_grad()`** at the start of each training step — gradients accumulate by default.
5. **Save `state_dict`, not the model** — `torch.save(model.state_dict(), path)` is more portable and robust than saving the full model.
