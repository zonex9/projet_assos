import { useState } from "react";
import Sidebar from "../components/Sidebar";
import ProductCard from "../components/ProductCard";

export default function Home() {
  const [cart, setCart] = useState([]);

  const products = [
    {
      id: 1,
      title: "Casque audio Bluetooth",
      price: 59.99,
      desc: "Son clair, autonomie 20h."
    },
    {
      id: 2,
      title: "Clavier mécanique compact",
      price: 79.99,
      desc: "Switches tactiles, rétroéclairage."
    }
  ];

  function addToCart(product) {
    setCart(prev => [...prev, product]);
  }

  function removeFromCart(index) {
    setCart(prev => prev.filter((_, i) => i !== index));
  }

  return (
    <div className="max-w-5xl mx-auto px-4 py-6 flex gap-6">
      <Sidebar cart={cart} removeFromCart={removeFromCart} />

      <main className="flex-1">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {products.map(prod => (
            <ProductCard
              key={prod.id}
              product={prod}
              addToCart={addToCart}
            />
          ))}
        </div>
      </main>
    </div>
  );
}
