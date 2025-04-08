import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios"; // Si deseas obtener datos desde una API
import Swal from "sweetalert2";

const UserDataTable = () => {
  const [data, setData] = useState([]); // Datos para la tabla
  const [loading, setLoading] = useState(true); // Estado de carga
  const [editUser, setEditUser] = useState(null);


  const accessToken = localStorage.getItem("accessToken");
  const refreshToken = localStorage.getItem("refreshToken");

    const createAxiosInstance = axios.create({
      baseURL: "http://127.0.0.1:8000",
      headers: { Authorization: `Bearer ${accessToken}` },
    });

    createAxiosInstance.interceptors.response.use(
      (response) => response,
      async (error) => {
        if (
          error.response &&
          error.response.status === 401 &&
          error.response.data.detail === "Authentication credentials were not provided."
        ) {
          try {
            const response = await axios.post("http://127.0.0.1:8000/api/token/refresh/", {
              refresh: refreshToken,
            });
  
            const newAccessToken = response.data.access;
            localStorage.setItem("accessToken", newAccessToken);
            
            error.config.headers.Authorization = `Bearer ${newAccessToken}`;
            return axiosInstance(error.config);
          } catch (refreshError) {
            console.error("No se pudo refrescar el token", refreshError);
            await Swal.fire({
              title: "Sesión expirada",
              text: "No se pudo refrescar tu sesión. Por favor, vuelve a iniciar sesión.",
              icon: "warning",
              confirmButtonText: "OK",
            });
            return Promise.reject(refreshError);
          }
        }
        return Promise.reject(error);
      }
    );


    const handleDelete = (userId) => {
      Swal.fire({
        title: "¿Estás seguro?",
        text: "Esta acción eliminará al usuario.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#d33",
        cancelButtonColor: "#3085d6",
        confirmButtonText: "Sí, eliminar",
        cancelButtonText: "Cancelar",
      }).then((result) => {
        if (result.isConfirmed) {
          createAxiosInstance
            .delete(`/users/api/${userId}/`)
            .then(() => {
              Swal.fire("Eliminado", "Usuario eliminado correctamente.", "success");
              fetchUsers();
            })
            .catch(() => {
              Swal.fire("Error", "No se pudo eliminar el usuario.", "error");
            });
        }
      });
    };


    const handleUpdate = () => {
      createAxiosInstance
        .put(`/users/api/${editUser.id}/`, editUser)
        .then(() => {
          Swal.fire("Actualizado", "Usuario actualizado correctamente.", "success");
          fetchUsers();
          setEditUser(null);
        })
        .catch(() => {
          Swal.fire("Error", "No se pudo actualizar el usuario.", "error");
        });
    };

  // Configuración de columnas
  const columns = [
    {
      name: "Nombre",
      selector: (row) => row.name, // Selector de datos
      sortable: true, // Habilitar ordenamiento
    },
    {
      name: "Email",
      selector: (row) => row.email,
      sortable: true,
    },
    {
      name: "Teléfono",
      selector: (row) => row.tel,
    },
    {
      name: "Acciones",
      cell: (row) => (
        <span>
          <button
            className="btn btn-warning me-4"
            onClick={() => setEditUser(row)}
          >
            <i className="bi bi-pencil"></i>
          </button>
          <button
            className="btn btn-danger me-4"
            onClick={() => handleDelete(row.id)}
          >
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  const fetchUsers = () => {
    const currentUserId = localStorage.getItem("userId");
    setLoading(true);
    createAxiosInstance
      .get("/users/api/")
      .then((response) => {
        const filteredData = response.data.filter(user => user.id.toString() !== currentUserId);
      setData(filteredData);
      setLoading(false);
      })
      .catch((error) => {
        console.error("Error al cargar los datos:", error);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div>
      <h3>Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />
       {editUser && (
        <div className="modal fade show d-block" tabIndex="-1">
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Editar Usuario</h5>
                <button
                  type="button"
                  className="btn-close"
                  onClick={() => setEditUser(null)}
                ></button>
              </div>
              <div className="modal-body">
                <div className="mb-3">
                  <label className="form-label">Nombre</label>
                  <input
                    type="text"
                    className="form-control"
                    value={editUser.name}
                    onChange={(e) =>
                      setEditUser({ ...editUser, name: e.target.value })
                    }
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Email</label>
                  <input
                    type="email"
                    className="form-control"
                    value={editUser.email}
                    onChange={(e) =>
                      setEditUser({ ...editUser, email: e.target.value })
                    }
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Teléfono</label>
                  <input
                    type="text"
                    className="form-control"
                    value={editUser.tel}
                    onChange={(e) =>
                      setEditUser({ ...editUser, tel: e.target.value })
                    }
                  />
                </div>
              </div>
              <div className="modal-footer">
                <button
                  className="btn btn-secondary"
                  onClick={() => setEditUser(null)}
                >
                  Cancelar
                </button>
                <button className="btn btn-primary" onClick={handleUpdate}>
                  Guardar cambios
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default UserDataTable;
