export default function Header() {
  return (
    <header className="bg-white shadow-md">
      <div className="max-w-5xl mx-auto px-4 py-4 flex items-center justify-between">
        <h1 className="text-xl font-semibold">Boutique</h1>
        <nav className="hidden md:flex gap-4 items-center">
          <a href="#" className="text-sm hover:underline">Accueil</a>
          <a href="#" className="text-sm hover:underline">Produits</a>
          <a href="#" className="text-sm hover:underline">Contact</a>
        </nav>
      </div>
    </header>
  );
}
