import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/home";
import Profile from "./pages/Profile"; // ajoute ta page Profil

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50 text-gray-800 flex flex-col">
        <Header />

        <main className="flex-1">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/profile" element={<Profile />} />
            {/* ajoute d'autres routes ici si besoin */}
          </Routes>
        </main>

        <Footer />
      </div>
    </Router>
  );
}

export default App;
