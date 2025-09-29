import React, { useState, useEffect } from "react";

const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function HabitList() {
  const [habits, setHabits] = useState([]);
  const [name, setName] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchHabits();
  }, []);

  async function fetchHabits() {
    setLoading(true);
    try {
      const res = await fetch(`${API}/habitos`);
      const data = await res.json();
      setHabits(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  async function addHabit(e) {
    e && e.preventDefault();
    if (!name.trim()) return;
    await fetch(`${API}/habitos`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nombre: name }),
    });
    setName("");
    fetchHabits();
  }

  async function toggle(h) {
    await fetch(`${API}/habitos/${h.id}/completo`, { method: "POST" });
    fetchHabits();
  }

  async function removeHabit(h) {
    if (!window.confirm(`Borrar "${h.name}"?`)) return;
    await fetch(`${API}/habitos/${h.id}`, { method: "DELETE" });
    fetchHabits();
  }

  return (
    <div>
      <form className="add-form" onSubmit={addHabit}>
        <input
          placeholder="Nuevo hábito (ej. Beber agua)"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <button type="submit">Agregar</button>
      </form>

      {loading ? <p>Cargando...</p> : null}

      <div style={{ marginTop: 12 }}>
        {habits.length === 0 ? (
          <p>No hay hábitos — agrega el primero.</p>
        ) : (
          habits.map((h) => (
            <div key={h.id} className="habit-item">
              <div className="habit-left">
                <input
                  type="checkbox"
                  checked={h.completed_today}
                  onChange={() => toggle(h)}
                />
                <div>
                  <div style={{fontWeight:600}}>{h.name}</div>
                  <div style={{fontSize:12, color:"#666"}}>Creado: {new Date(h.created_at).toLocaleDateString()}</div>
                </div>
              </div>

              <div>
                <button className="small-btn" onClick={() => removeHabit(h)}>🗑️</button>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
