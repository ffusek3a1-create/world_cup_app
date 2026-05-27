import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom"
import Groups   from "./pages/Groups"
import Schedule from "./pages/Schedule"
import Venues   from "./pages/Venues"

export default function App() {
  return (
    <BrowserRouter>
      <nav className="bg-blue-900 text-white px-6 py-4 flex gap-6 text-sm font-semibold">
        <span className="mr-auto text-lg font-bold tracking-wide">⚽ WC 2026</span>
        <NavLink to="/"         className={({isActive}) => isActive ? "text-yellow-400" : "hover:text-yellow-300"}>Groups</NavLink>
        <NavLink to="/schedule" className={({isActive}) => isActive ? "text-yellow-400" : "hover:text-yellow-300"}>Schedule</NavLink>
        <NavLink to="/venues"   className={({isActive}) => isActive ? "text-yellow-400" : "hover:text-yellow-300"}>Venues</NavLink>
      </nav>
      <main className="min-h-screen bg-gray-50 p-6">
        <Routes>
          <Route path="/"         element={<Groups />} />
          <Route path="/schedule" element={<Schedule />} />
          <Route path="/venues"   element={<Venues />} />
        </Routes>
      </main>
    </BrowserRouter>
  )
}