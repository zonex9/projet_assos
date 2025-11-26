export default function Profile() {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center py-10 px-4">
      
      {/* Logo */}
      <div className="mb-6">
        <div className="w-20 h-20 bg-blue-600 text-white rounded-full flex items-center justify-center text-3xl font-bold shadow-lg">
          HB
        </div>
      </div>

      {/* Card Profil */}
      <div className="bg-white rounded-2xl shadow-md p-6 w-full max-w-md">
        <h2 className="text-xl font-semibold text-gray-800 mb-4 text-center">
          Mon Profil
        </h2>

        <div className="space-y-4">

          {/* Nom */}
          <div>
            <p className="text-xs text-gray-500">Nom</p>
            <p className="text-sm font-medium">Baabit</p>
          </div>

          {/* Prénom */}
          <div>
            <p className="text-xs text-gray-500">Prénom</p>
            <p className="text-sm font-medium">Hatim</p>
          </div>

          {/* Email */}
          <div>
            <p className="text-xs text-gray-500">Email</p>
            <p className="text-sm font-medium">hatim@example.com</p>
          </div>

          {/* Localisation */}
          <div>
            <p className="text-xs text-gray-500">Localisation</p>
            <p className="text-sm font-medium">Lyon, France</p>
          </div>

        </div>

        {/* Bouton Modifier */}
        <button className="w-full mt-6 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition">
          Modifier le profil
        </button>
      </div>

    </div>
  );
}
