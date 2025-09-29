import React, { useEffect, useState } from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function ProgressChart() {
  const [items, setItems] = useState([]);
  const [apiError, setApiError] = useState(false);

  useEffect(() => {
    fetchProgress();
  }, []);

  async function fetchProgress() {
    setApiError(false); 
    try {
      const res = await fetch(`${API}/progreso?days=7`);
      
      if (!res.ok) {
        setApiError(true);
        throw new Error(`Error de red: ${res.status}`);
      }
      
      const data = await res.json();
      setItems(data);
    } catch (error) {
      console.error("Error al obtener el progreso:", error);
      setApiError(true);
    }
  }

  // --- SOLUCIÓN AL UNCAUGHT TYPEERROR ---
  // 1. Filtramos 'items' para crear un array limpio.
  // Solo incluimos elementos 'it' que NO sean null/undefined Y que tengan la propiedad 'date'.
  const validItems = items.filter(it => it && it.date);
  
  if (validItems.length === 0 && !apiError) {
      // Usamos el estado original para mostrar 'Cargando...' solo si aún no hay respuesta.
      if (items.length === 0) {
          return <div style={{ maxWidth: '600px', margin: 'auto' }}><p>Cargando progreso...</p></div>;
      }
      // Si la carga fue exitosa pero no había datos válidos:
      return <div style={{ maxWidth: '600px', margin: 'auto' }}><p>No hay datos de progreso disponibles para los últimos 7 días.</p></div>;
  }
  
  if (apiError) {
      return <div style={{ maxWidth: '600px', margin: 'auto' }}><p>🚨 Error al cargar el progreso. Verifica la conexión con la API en: {API}</p></div>;
  }
  
  // 2. Mapeamos sobre el array limpio 'validItems'.
  const labels = validItems.map((it) => {
    // Aquí 'it.date' está garantizado de existir, eliminando el TypeError.
    const dateString = it.date.replace(/-/g, "/"); 
    const d = new Date(dateString);

    if (isNaN(d.getTime())) {
      console.warn(`Fecha inválida encontrada para el valor: ${it.date}`);
      return "Fecha Inválida";
    }

    return d.toLocaleDateString(undefined, { weekday: "short", day: "numeric" });
  });

  const counts = validItems.map((it) => it.count);
  
  // Si los datos limpios tienen un problema de formato interno (ej. cuenta no numérica)
  if (labels.includes("Fecha Inválida") || counts.some(c => typeof c !== 'number')) {
      return <div style={{ maxWidth: '600px', margin: 'auto' }}><p>Error: Los datos recibidos de la API tienen un formato inválido (problema de fechas o conteos).</p></div>;
  }

  // --- CONFIGURACIÓN DE LA GRÁFICA ---
  const data = {
    labels,
    datasets: [
      {
        label: "Hábitos completados",
        data: counts,
        backgroundColor: 'rgba(53, 162, 235, 0.5)',
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: "top" },
      title: { display: true, text: "Progreso últimos 7 días" },
    },
    scales: {
        y: {
            beginAtZero: true,
            ticks: { precision: 0 }
        }
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: 'auto' }}>
      <Bar data={data} options={options} />
    </div>
  );
}