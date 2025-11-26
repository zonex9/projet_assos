export default function Sidebar({ cart, removeFromCart }) {
  return (
    <aside className="w-64 bg-white rounded-2xl p-4 shadow-sm sticky top-6 h-fit">
      <h2 className="font-semibold mb-3">Navigation</h2>

      <ul className="space-y-2 text-sm">
        <li><a className="block py-2 px-3 rounded hover:bg-gray-100" href="#">Matériels</a></li>
        <li><a className="block py-2 px-3 rounded hover:bg-gray-100" href="#">Mes commandes</a></li>
      </ul>

      <div className="mt-6 border-t pt-4">
        <h3 className="font-semibold text-sm mb-2">Panier</h3>
        <div className="text-sm text-gray-600">
          Articles : <span className="font-medium">{cart.length}</span>
        </div>

        <ul className="mt-3 space-y-2 max-h-36 overflow-auto text-sm">
          {cart.length === 0 && <li className="text-xs text-gray-500">Panier vide</li>}

          {cart.map((p, i) => (
            <li key={i} className="flex justify-between">
              <div>
                <div className="font-medium">{p.title}</div>
                <div className="text-xs text-gray-500">{p.price.toFixed(2)} €</div>
              </div>

              <button
                onClick={() => removeFromCart(i)}
                className="ml-3 text-xs px-2 py-1 rounded bg-red-50 hover:bg-red-100"
              >
                retirer
              </button>
            </li>
          ))}
        </ul>

        {/* Bouton Valider */}
        {cart.length > 0 && (
          <button
            className="w-full mt-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition"
            onClick={() => alert("Panier validé !")}
          >
            Valider le panier
          </button>
        )}
      </div>
    </aside>
  );
}
