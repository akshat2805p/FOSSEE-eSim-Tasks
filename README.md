# FOSSEE eSim Tasks

This repository contains development tasks, scripting modules, and automation framework implementations completed during my summer fellowship at FOSSEE, IIT Bombay.

---

## 🚀 Task 1: KiCad Python API Integration & Action Plugin Framework

### 📝 Objective
Initialize a native programmatic workspace within KiCad 10.0 using the wrapped C++ `pcbnew` Python engine layer. This lays the groundwork for automated PCB layout manipulation and eventual hook integrations into the core eSim suite framework.

### 🛠️ Implementation Details
* **Script Placement:** Configured local environment architectures under the `10.0/scripting/plugins/` directory path.
* **Architecture:** Developed a standalone Python Action Plugin inheriting from `pcbnew.ActionPlugin`. Overrode the initialization hook (`defaults()`) to bind metadata and utilized standard decoupled UI messaging.

### 🔍 Technical Challenges & Resolution Log
1. **Scope Isolation (`ModuleNotFoundError`):** Discovered that the `pcbnew` namespace is bound strictly inside KiCad's internal runtime container binaries rather than the system's global interpreters. Shifted deployment from external script invocation to the native application execution layer.
2. **API Deprecation (`AttributeError`):** Resolved interface decouple crashes caused by the removal of `pcbnew.wxMessageBox` in modern KiCad versions. Patched layout by directly importing the native `wx` toolkit library callbacks (`wx.MessageBox`).

### 📦 Verifying Execution
1. Open the **KiCad PCB Editor** within an active project context.
2. Navigate to **Tools** $\rightarrow$ **External Plugins** $\rightarrow$ **Refresh Plugins**.
3. Select **Hello FOSSEE** from the macro manager interface layer to trigger the native confirmation dialog box.