const BASE = "http://127.0.0.1:8000"
 
export const getTeams   = () => fetch(`${BASE}/teams`).then(r => r.json())
export const getTeam    = (name) => fetch(`${BASE}/teams/${encodeURIComponent(name)}`).then(r => r.json())
export const getGroups  = () => fetch(`${BASE}/groups`).then(r => r.json())
export const getMatches = (stage) => fetch(`${BASE}/matches${stage ? `?stage=${encodeURIComponent(stage)}` : ""}`).then(r => r.json())
export const getVenues  = () => fetch(`${BASE}/venues`).then(r => r.json())
export const getVenue   = (name) => fetch(`${BASE}/venues/${encodeURIComponent(name)}`).then(r => r.json())