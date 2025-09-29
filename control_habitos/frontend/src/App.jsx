import React, { useState } from "react";
import HabitList from "./componentes/HabitList";
import ProgressChart from "./componentes/ProgressChart";

export default function App() {
  const [view, setView] = useState("habits"); // 'habits' o 'progress'

  return (
    <div className="app">
      <header>
        <h1>Control de Hábitos</h1>
        <div className="nav">
          <button onClick={() => setView("habits")} className={view==="habits"?"active":""}>Hábitos</button>
          <button onClick={() => setView("progress")} className={view==="progress"?"active":""}>Progreso</button>
        </div>
      </header>

      <main>
        {view === "habits" ? <HabitList /> : <ProgressChart />}
      </main>

      <footer>
        <small>Backend: http://localhost:8000 • Frontend: Vite</small>
      </footer>
    </div>
  );
}
