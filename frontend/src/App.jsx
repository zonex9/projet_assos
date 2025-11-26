import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/home";

function App() {
  return (
    <div className="min-h-screen bg-gray-50 text-gray-800 flex flex-col">
      <Header />
      <Home />
      <Footer />
    </div>
  );
}

export default App;
