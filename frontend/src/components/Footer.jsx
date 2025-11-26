export default function Footer() {
  return (
    <footer className="bg-white border-t mt-10">
      <div className="max-w-5xl mx-auto px-4 py-6 flex items-center justify-between text-sm text-gray-600">
        <div>© {new Date().getFullYear()} Boutique de prêt des matériels</div>
        <div>Mentions légales · Politique de confidentialité</div>
      </div>
    </footer>
  );
}
