# Guild Dispatch Engine: Automated Roster & Resource Management

## Overview
This project is a lightweight, backend Python application that automates the scheduling, resource allocation, and financial tracking for an adventurer's guild. By parsing JSON based databases of available personnel and upcoming contracts, the engine dynamically matches heroes to quests based on required roles, prevents double booking through state management, and calculates weekly profit margins via a custom terminal interface (CLI).

## Objectives
* Dynamically match available adventurers to specific quest requirements (e.g., finding an available "Defender" and "Pathfinder").
* Prevent scheduling conflicts by updating adventurer availability in real time once drafted.
* Track the operational cost of hired heroes against the gross quest payout to determine net profit.
* Render a clean, highly readable text based dispatch board using dynamic string formatting and justification.

## Technical Stack

| Purpose | Technology |
| :--- | :--- |
| **Language** | Python 3 |
| **Data Storage** | JSON |
| **File Traversal** | `pathlib` |
| **Environment** | Standard Terminal / Command Line |
| **Core Concepts** | Dictionary Mapping, Modular Functions, State Management, String Formatting |

## Data Architecture 
The system relies on two local JSON databases to simulate external API data ingestion:
* `adventurers.json`: Contains the personnel roster, including each hero's unique ID, combat roles, daily operational cost, and availability schedule.
* `quests.json`: Contains the weekly contract board, outlining the target day, exact roles required for success, and the total gross payout in gold.

## System Workflow

**1. Data Ingestion & Pathing**
* Utilises Python's `pathlib` to establish absolute file paths, ensuring the script can run from any directory without breaking data links.
* Parses raw JSON data into usable Python dictionaries and lists.

**2. Drafting & Validation Logic (`guild_tools.py`)**
* Iterates through the weekly quest requirements.
* Calls custom modular functions to cross reference the required roles against the roster's availability. 
* Returns a validated list of specific hero names capable of completing the contract.

**3. State Update & Financial Processing (`dispatcher.py`)**
* Updates the availability calendar of drafted heroes to prevent double booking on the same day.
* Calculates the net profit by subtracting the combined operational cost of the drafted team from the quest's total payout.
* Appends the finalised data (Quest, Team, Profit) to a weekly schedule dictionary.

**4. CLI Rendering**
* Utilises `.ljust()`, `.rjust()`, and `.center()` string methods to dynamically render a bordered, 4 column ledger in the terminal.
* Gracefully handles empty schedule days with fallback values.

## Repository Structure

guild-dispatch-engine/

├── data/

│   ├── adventurers.json  

│   └── quests.json     

├── scripts/

│   ├── dispatcher.py       

│   └── guild_tools.py      

├── __pycache__/         

└── README.md