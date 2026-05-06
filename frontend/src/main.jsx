import React, { useEffect, useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import {
  Area,
  AreaChart,
  CartesianGrid,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
  BarChart,
  Bar,
} from 'recharts';
import { CloudSun, Wind, Droplets, ThermometerSun, AlertTriangle, RefreshCw } from 'lucide-react';
import './styles.css';

const API_BASE = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8000';

function StatCard({ icon, label, value, sub }) {
  return (
    <div className="stat-card">
      <div className="stat-icon">{icon}</div>
      <div>
        <p className="muted">{label}</p>
        <h3>{value}</h3>
        {sub && <small>{sub}</small>}
      </div>
    </div>
  );
}

function AlertPill({ alert }) {
  return <div className={`alert-pill ${alert.severity}`}>{alert.label}</div>;
}

function App() {
  const [locations, setLocations] = useState([]);
  const [selectedId, setSelectedId] = useState(1);
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  async function loadLocations() {
    const response = await fetch(`${API_BASE}/locations`);
    if (!response.ok) throw new Error('Backend is not running or /locations failed');
    const data = await response.json();
    setLocations(data);
    if (data.length) setSelectedId(data[0].id);
  }

  async function loadSummary(id = selectedId) {
    setLoading(true);
    setError('');
    try {
      const response = await fetch(`${API_BASE}/summary/${id}`);
      if (!response.ok) throw new Error('Unable to load forecast summary');
      const data = await response.json();
      setSummary(data);
    } catch (err) {
      setError(err.message || 'Something went wrong');
    } finally {
      setLoading(false);
    }
  }

  async function generateReport() {
    if (!summary) return;
    const response = await fetch(`${API_BASE}/reports/${selectedId}`, { method: 'POST' });
    const data = await response.json();
    alert(`Report generated: ${data.report_path}`);
  }

  useEffect(() => {
    loadLocations().catch((err) => setError(err.message));
  }, []);

  useEffect(() => {
    if (selectedId) loadSummary(selectedId);
  }, [selectedId]);

  const current = summary?.current;
  const daily = summary?.daily || [];
  const hourly = summary?.hourly || [];
  const selectedCity = summary?.location?.name || 'Weather Dashboard';

  const rainScore = useMemo(() => {
    if (!daily.length) return 0;
    return Math.round(daily.reduce((sum, row) => sum + Number(row.rain_prob || 0), 0) / daily.length);
  }, [daily]);

  return (
    <main>
      <section className="hero">
        <div>
          <p className="eyebrow">Python + FastAPI + React Project</p>
          <h1>Weather Forecast & Alert Application</h1>
          <p className="hero-text">
            Track city-wise weather, visualize hourly and weekly trends, and receive rule-based alerts for rain,
            heat, wind, and UV risk.
          </p>
        </div>
        <div className="hero-panel">
          <CloudSun size={54} />
          <h2>{selectedCity}</h2>
          <p>{current ? `${current.temp_c}°C • Humidity ${current.humidity}%` : 'Loading forecast...'}</p>
        </div>
      </section>

      <section className="toolbar">
        <select value={selectedId} onChange={(e) => setSelectedId(Number(e.target.value))}>
          {locations.map((location) => (
            <option key={location.id} value={location.id}>{location.name}</option>
          ))}
        </select>
        <button onClick={() => loadSummary(selectedId)} disabled={loading}>
          <RefreshCw size={16} /> Refresh
        </button>
        <button className="secondary" onClick={generateReport}>Generate CSV Report</button>
      </section>

      {error && <div className="error">{error}</div>}

      <section className="stats-grid">
        <StatCard icon={<ThermometerSun />} label="Temperature" value={current ? `${current.temp_c}°C` : '--'} sub="Current condition" />
        <StatCard icon={<Droplets />} label="Humidity" value={current ? `${current.humidity}%` : '--'} sub="Relative humidity" />
        <StatCard icon={<Wind />} label="Wind Gust" value={current ? `${current.wind_gust_ms} m/s` : '--'} sub="Next hour estimate" />
        <StatCard icon={<AlertTriangle />} label="Rain Risk" value={`${rainScore}%`} sub="7-day average probability" />
      </section>

      <section className="alerts">
        <h2>Weather Alerts</h2>
        <div className="alert-list">
          {(summary?.alerts || []).map((alert) => <AlertPill key={alert.code} alert={alert} />)}
        </div>
      </section>

      <section className="charts-grid">
        <div className="chart-card wide">
          <h2>Next 24 Hours Temperature</h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={hourly}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="ts" hide />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="temp_c" strokeWidth={3} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-card">
          <h2>7-Day Rain Forecast</h2>
          <ResponsiveContainer width="100%" height={280}>
            <AreaChart data={daily}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Area type="monotone" dataKey="rain_mm" strokeWidth={2} />
            </AreaChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-card">
          <h2>Daily Max Temperature</h2>
          <ResponsiveContainer width="100%" height={280}>
            <BarChart data={daily}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="tmax_c" radius={[8, 8, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </section>
    </main>
  );
}

createRoot(document.getElementById('root')).render(<App />);
