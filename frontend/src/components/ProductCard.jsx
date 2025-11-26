export default function ProductCard({ product, addToCart }) {
  return (
    <article className="bg-white rounded-2xl p-6 shadow-md flex flex-col justify-between">
      <div>
        <h3 className="text-lg font-semibold">{product.title}</h3>
        <p className="mt-2 text-sm text-gray-600">{product.desc}</p>
      </div>

      <div className="mt-4 flex items-center justify-between">
        <div className="text-xl font-bold">{product.price.toFixed(2)} €</div>
        <button
          onClick={() => addToCart(product)}
          className="inline-flex px-4 py-2 rounded-2xl bg-blue-600 text-white hover:bg-blue-700"
        >
          Ajouter au panier
        </button>
      </div>
    </article>
  );
}
