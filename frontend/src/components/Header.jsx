import { Link } from "react-router-dom";


export default function Header() {
  return (
    <header className="bg-white shadow-md">
      <div className="max-w-5xl mx-auto px-4 py-4 flex items-center justify-between">
        <h1 className="text-xl font-semibold">Boutique</h1>
        <nav className="hidden md:flex gap-4 items-center">
          <a href="/" className="text-sm hover:underline">Accueil</a>
          <Link to="/profile" className="text-sm hover:underline">Mon profil</Link>
          <a href="http://localhost:5000/v2/" className="text-sm hover:underline">Association</a>
        </nav>
      </div>
    </header>
  );
}
